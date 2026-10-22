# HIRING PORTAL WEB APPLICATION 💼

A 3rd-year end-of-year project built with Django and PostgreSQL. The platform connects job seekers and recruiters, allowing companies to post job listings and manage applications while giving candidates tools to build their profiles and track their submissions.

## FEATURES ✨

- **Job Postings** — Recruiters can create and manage job listings with detailed descriptions, requirements, and deadlines.
- **CV Management** — Job seekers can create and update profiles with personal information, skills, education, and uploaded documents.
- **Job Search** — Browse job offers and filter listings using available company and sector criteria.
- **Application Tracking** — Submit job applications and view their current status.
- **User Authentication** — Register and log in as a job seeker, with recruiter access managed through associated recruiter profiles.
- **Recruiter Management** — Review candidate applications and update their acceptance or rejection status.
- **Admin Dashboard** — Administrators can manage users, job listings, and applications through Django's administration interface.

## TECHNOLOGIES 🚀

- **Python** — Programming language used for backend development.
- **Django** — High-level Python web framework for building the application.
- **PostgreSQL** — Relational database management system.
- **Django ORM** — Database access and model management framework.
- **HTML/CSS/JavaScript** — Frontend technologies for building the user interface.
- **Bootstrap** — Frontend framework for responsive, mobile-first design.

## DEMO 🎬

Watch the demo on [YouTube](https://youtu.be/wzjV01i2Dl8).

## PREREQUISITES 📋

Before getting started, ensure you have the following:

- **Python and pip** — Required to install dependencies and run the application.
- **Django** — A compatible version of the framework.
- **PostgreSQL** — A local or accessible database instance.
- **PostgreSQL Adapter** — A compatible Python adapter such as `psycopg2`.
- **Pillow** — Required for image fields and uploaded images.

The source files reference Django 4.0.4, but no dependency manifest or exact compatible Python version is supplied.

Windows is the recommended environment for the current source because it contains a Windows-specific Python import. Running on Linux or macOS would require correcting that import.

## INSTALLATION ⚙️

1. Clone the repository to your local machine.
2. Open PowerShell in the repository root and create a Python virtual environment: `py -m venv .venv`.
3. Activate the virtual environment: `.\.venv\Scripts\Activate.ps1`.
4. Install compatible versions of Django, the PostgreSQL adapter, and Pillow. The repository does not include a `requirements.txt`, `pyproject.toml`, or other dependency manifest, so the original tested package versions are unavailable.
5. Create a PostgreSQL database for the application.
6. Open `wadifati/settings.py` and update the `DATABASES` configuration with your database connection details.
7. Apply the existing database migrations: `python manage.py migrate`.
8. Create a Django administrator account: `python manage.py createsuperuser`.
9. Use the administration interface to create or associate recruiter profiles with user accounts and configure the relevant company and sector information. Public registration creates job seeker accounts rather than automatically provisioning recruiter profiles.
10. Ensure the configured `media/` directory is writable for uploaded photos, CVs, and other documents.
11. Start the development server: `python manage.py runserver`.
12. Open `http://127.0.0.1:8000/` in your browser. The Django administration interface is available at `/admin/`.

The source includes database migrations, but the original dependency versions and a complete tested installation environment are not available. The setup above reflects the repository's structure and configuration rather than a verified fresh installation.

## CONTRIBUTING 🤝

Contributions are welcome! Please follow these guidelines:

1. Follow the existing project structure and coding conventions.
2. Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.
3. Test your changes locally whenever possible.
4. Update the documentation when introducing new features or changing existing functionality.

## LICENSE 📄

This project is licensed under the [MIT License](LICENSE).

## CONTACT 📧

For any questions or feedback, reach out at [contact@aimanecouissi.com](mailto:contact@aimanecouissi.com).
