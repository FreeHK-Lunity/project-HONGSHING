# project-HONGSHING

project-HONGSHING OMSI2 map.

## CHAPTER 1 --- Installing Git

 Download the latest version of Git from this website. : <https://git-scm.com/downloads>
 Choose the 64/32 bit version.
 After the file is downloaded, install it in the system. Once installed, go to your Start Menu.
 Select Launch Git Bash, then click on finish. The Git Bash is now launched.
 To verify that Git is installed correctly and functioning properly, run this command in the terminal.
 `git –version`

## CHAPTER 2 --- Forking the repository

 Go to <https://github.com/FreeHK-Lunity/project-HONGSHING>>
 Inside the repository, there is a fork button.
 Press the fork button.
 In the `Create a new fork` page, Click on the `Create fork` button.
You have successfully created a fork of the main project-HONGSHING repository!

## CHAPTER 3 --- Using Git

 On your OMSI 2 main folder, right click on an empty space.
 If you are on Windows 11, click on `Open In Terminal`.
 If you are on Windows 10, click on `Open Git Bash here`.
 Run the following command inside the terminal.
 `git clone https:/[insert your username here]:[insert your password here]@github.com/[insert your username here]/project-HONGSHING.git`
 Inside the `project-HONGSHING` folder, move the maps folder to your OMSI 2 folder.
You are set for map development now!

## CHAPTER 4 --- Pushing to your repository

 Please install Vim from the following website. <https://www.vim.org/download.php>
 Press on the `self installing executable` hyperlink.
 Follow the steps to install the application.
 Go to your Git Bash terminal.
 Type the following command to change to your OMSI 2 `project-HONGSHING` folder inside the terminal.
 ```cd F:```
 ```cd OMSI [tab]```
 ```cd project [tab]```
 After you have copied the edited map into the `project-HONGSHING` folder, type the following commands into the Git Bash terminal.
 ```git add *```
 ```git commit -a```
 Inside your Git Bash window, press enter.
 You should have started a new line.
 Please write about what you have edited in that line.
 After you finish typing the commit message, press [Esc], then type `:x` `[Enter]` and `:q` `[Enter]`
 Finishing the commit process, you can now input the following command.
 ```git push```
 Your changes will now be updated in your repository.

## CHAPTER 5 --- Submitting your pull request

 Go to the pull request page of the repository.(<https://github.com/FreeHK-Lunity/project-HONGSHING/pulls>)
 Click on `New pull request`
 Click on `compare across forks`
 Click on `compare`
 Choose your own repository.
 Click on `Create pull request`
 Type what you have edited in the title.
 If possible, add screenshots about what you have edited.
 Click on `Create pull request`

You have successfully created a pull request! Please wait patiently for the main map editors to approve your pull request.

## BEWARE

 You have to copy your whole `maps\project-HONGSHING` folder to the `project-HONGSHING` inside your main OMSI 2 folder whenever have you finish editing your map.
