## Executeables

To create executeables in python, we can use a utility like `PyInstaller`.

Follow the steps below to create a simple, one-file executeable.

1. Install `PyInstaller`.
```bash
pip install pyinstaller
```

2. Navigate to the directory of your project.

3. Use the following command to create the executeable.
```bash
pyinstaller --onefile your_script.py
```

4. You can now execute the file `./dist/your_script.py`.

