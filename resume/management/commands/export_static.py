import os
import shutil
from pathlib import Path
from django.core.management.base import BaseCommand
from django.test import Client
from django.conf import settings


class Command(BaseCommand):
    help = "Exports the Django resume website to a static 'docs/' directory for GitHub Pages hosting"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Exporting website for GitHub Pages..."))

        base_dir = Path(settings.BASE_DIR)
        docs_dir = base_dir / "docs"

        # Ensure docs directory exists
        docs_dir.mkdir(parents=True, exist_ok=True)

        # 1. Render index.html using Django client
        client = Client()
        response = client.get('/')
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f"Failed to render homepage (HTTP {response.status_code})"))
            return

        html_content = response.content.decode('utf-8')

        # Convert static paths to relative for GitHub Pages compatibility
        html_content = html_content.replace('href="/static/', 'href="./static/')
        html_content = html_content.replace('src="/static/', 'src="./static/')
        html_content = html_content.replace('href="/#', 'href="#')
        html_content = html_content.replace('action="/#contact"', 'action="mailto:dnhp281999@gmail.com"')
        html_content = html_content.replace('Dev Nareshkumar Patel', 'Dev Patel')

        index_file = docs_dir / "index.html"
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        # 2. Copy static files to docs/static
        static_src = base_dir / "resume" / "static" / "resume"
        static_dest = docs_dir / "static" / "resume"
        shutil.copytree(static_src, static_dest, dirs_exist_ok=True)

        # 3. Add .nojekyll for GitHub Pages
        nojekyll_file = docs_dir / ".nojekyll"
        nojekyll_file.touch()

        self.stdout.write(self.style.SUCCESS(
            f"Successfully exported static site to {docs_dir}\n"
            f"Now you can commit the 'docs' folder and enable GitHub Pages in your repo settings!"
        ))

