# Project-HONGSHING

Welcome to the Project-HONGSHING OMSI2 map contribution guide! This guide will walk you through the steps of contributing to the map.

## Chapter 1: Installing Git

1. Download the latest version of Git from the [Git website](https://git-scm.com/downloads).
2. Choose the appropriate 64-bit or 32-bit version for your system.
3. Install Git on your system.
4. Launch Git Bash from the Start Menu.
5. To verify that Git is installed correctly and functioning properly, run this command in the terminal:

   ``` git
   git --version
   ```

## Chapter 2: Forking the Repository

1. Go to the [Project-HONGSHING repository](https://github.com/FreeHK-Lunity/project-HONGSHING).
2. Click on the "Fork" button in the top right corner of the page.
3. In the "Create a new fork" page, click on the "Create fork" button.

### Congratulations! You have successfully created a fork of the main Project-HONGSHING repository.

## Chapter 3: Using Git

1. Right-click on an empty space in your OMSI 2 main folder.
2. If you are on Windows 11, click on "Open in Terminal". If you are on Windows 10, click on "Open Git Bash here".
3. Run the following command inside the terminal:

``` git
git clone https://github.com/[insert your username here]/project-HONGSHING.git
```

4. Move the "maps" folder from the "project-HONGSHING" folder to your OMSI 2 folder.

### Great! You are now ready for map development.

## Chapter 4: Pushing to Your Repository

1. Install Vim from the [Vim website](https://www.vim.org/download.php).
2. Follow the steps to install the application.
3. Go to your Git Bash terminal.
4. Type the following commands to change to your OMSI 2 "project-HONGSHING" folder inside the terminal:

   ``` cmd
   cd F:
   cd OMSI [tab]
   cd project [tab]
   ```
 ## This is an example prompt to change to the OMSI 2 "project-HONGSHING" folder. The Commands will change depending on where you put your OMSI folder.
5. After you have edited the map, copy it into the "project-HONGSHING" folder.
6. Type the following commands into the Git Bash terminal:

   ``` cmd
   git add *
   git commit -a
   ```

7. Inside your Git Bash window, press "Enter".
8. Write a commit message about what you have edited in that line.
9. After you finish typing the commit message, press "Esc", then type

    ``` cmd
    :x [Enter]  
    :q [Enter]
    ```

10. Finish the commit process by inputting the following command: `git push`.

### Your changes will now be updated in your repository.

## Chapter 5: Submitting Your Pull Request

1. Go to the [pull request page](https://github.com/FreeHK-Lunity/project-HONGSHING/pulls) of the repository.
2. Click on "New pull request".
3. Click on "compare across forks".
4. Click on "compare".
5. Choose your own repository.
6. Click on "Create pull request".
7. Type a title that describes what you have edited.
8. If possible, add screenshots of your edits.
9. Click on "Create pull request".

### Congratulations! You have successfully created a pull request. Please wait patiently for the main map editors to approve your pull request.

## Note

Remember to copy your whole "maps\project-HONGSHING" folder to the "project-HONGSHING" folder inside your main OMSI 2 folder whenever you finish editing your map.
