# Installing the Anaconda Python distribution

- Anaconda is a distribution that includes both Python and numerous packages
  required to perform scientific computing. 
- You should prefer Anaconda over a "bare minimum" Python installer
  such as the one distributed via [python.org](https://www.python.org/downloads/).
- You should prefer Anaconda over the Python distribution shipped with
  your operating system (macOS and Linux).

## Installation

1. Download the installer from the [Anaconda website](https://www.anaconda.com/download/success).
    - **No registration is required**, skip it if prompted.
    - You need to choose the correct installer for your platform.
    - For macOS, this depends on your hardware (*Apple Silicon* or *Intel*).
      If you are unsure which one you are using, consult 
      [this guide](https://support.apple.com/guide/mac-help/get-system-information-about-your-mac-syspr35536/mac).
2. Running the installer should be straightforward, but you can consult
    [this guide](https://docs.anaconda.com/anaconda/install/) 
    if needed.

## Creating an Anaconda environment

-   The Anaconda installation comes with a default environment called `base`
    which contains most if not all packages required for this course.
-   Nevertheless, you should create a course-specific environment
    from the environment definition file [`environment.yml`](../environment.yml).

    This has the advantage that the Python and package versions you use 
    are the same as those used by the instructor.

-   To do so, use the Anaconda Prompt (Windows) or the terminal (macOS)
    and run the following command:
    ```bash
    conda env create -f environment.yml
    ```
    Note that this must be run from the directory where `environment.yml`
    is located. It creates an environment called `FIE463`.

### Note for macOS users on Intel chips

- Apple and Anaconda have 
   [terminated support](https://www.anaconda.com/blog/intel-mac-package-support-deprecation) 
   for Intel-based Macs,
   and hence some of the packages in `environment.yml` may not be
   available for your platform.

- There is an alternative environment definition file 
   [`environment-intel-mac.yml`](../environment-intel-mac.yml) 
   for such cases. Create the environment as follows:
    ```bash
    conda env create -f environment-intel-mac.yml
    ```
- Note that some packages will be outdated and may be missing some 
  of the features we use in the course.