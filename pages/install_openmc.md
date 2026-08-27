# Installing OpenMC for NE 630 on Windows

Use the OpenMC Class Windows installer provided for this course. It installs
OpenMC, Python, JupyterLab, the scientific Python packages we will use, and the
course nuclear data in one local environment.

## Install

1. Download `OpenMC-Class-2026.1.dev0-Windows-x86_64.exe` from the course
   Canvas site.
2. Run the installer.
3. Select **Just Me** unless you have a specific reason to install for all users.
4. Keep the default install location:

   ```
   %LOCALAPPDATA%\OpenMC-Class
   ```

5. Leave **Create shortcuts** and **Run the post-install script** checked.
6. Click **Install** and wait for the setup wizard to finish. This can take
   several minutes.

## Start OpenMC

After installation, open **OpenMC JupyterLab** from the Windows Start menu. Use
that JupyterLab shortcut for course notebooks.

The installer configures the bundled course nuclear data automatically. When
using this installer, you do not need to add a manual `cross_sections.xml` path
to your notebooks.

## Quick Check

In a new notebook, run:

```python
import os
import openmc

print(openmc.__version__)
print(os.environ.get("OPENMC_CROSS_SECTIONS"))
```

The second line should print a path inside your `OpenMC-Class` installation.

If you see a command-window prompt that says no OpenMC nuclear data path is
configured, stop and ask for help before running course examples.
