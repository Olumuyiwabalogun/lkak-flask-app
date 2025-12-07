# cPanel Deployment Steps (summary)
1. Zip the project directory (keep the structure intact).
2. Login to cPanel -> File Manager -> Upload the zip to your desired folder (e.g. ~/apps/lkak).
3. Extract the zip in File Manager.
4. In cPanel, go to "Setup Python App" (or "Python App") and create a new application:
- Choose Python version (3.11+ recommended).
- App directory: the folder where app.py is located.
- Application entry point: app:app
- Passenger log file: keep default.
5. Use the virtual environment terminal in cPanel or SSH to run: pip install -r requirements.txt
6. Configure .env with real SECRET_KEY and DATABASE_URL (use MySQL database created in cPanel MySQL Databases)
7. Run migrations (from the virtualenv): flask db upgrade
8. Ensure static files are accessible. If needed, configure DocumentRoot or add rewrite rules.
9. Visit the app URL provided by cPanel.