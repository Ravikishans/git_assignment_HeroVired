# git_assignment_HeroVired
step1- creating a git-hub repository by the name of 'git-_assignment-HeroVired'
step2- clicking on the 'code' menu and couping the 'https' url
step3- opening git bash in your computer and cloning the repository by "git clone" command in respective folder
now when the repository is cloned in local computer we can start the tasks

TASK 1--

step1- for starting the task 1 we have to creat a new branch named "dev" and checkingout in it by command "git checkout -b dev"
step3- now we have to create a new python script named "CalculatorPlus.py" by               command "touch CalculatorPlus.py"
step4- now we can open vscode by command "code ."
step5- now we write python script in vscode for calculating add,substract,devide and multiply
step6- now in git bash add and commit the code in dev branch by commands "git add ." and "git commit -m "version1""
step6- come back to main branch and merge dev branch into main branch then push the code to the repository by commands- "git checkout main" ; "git init" ; "git commit -a" ; "git push"
step7- 


TASK 2--

step1- install Git LFS on your system from website https://git-lfs.github.com/
step2- now initialize Git LFS in your repository. command "git lfs install"
step3- now create a branch named lfs and checkout in it. command "git checkout -b lfs"
step4- creating a large binary file in git bash. command- "dd if=/dev/urandom of=large_file.bin bs=1M count=200"
step5- now add commit and push to main and the merge and the push it to the repository. commands- "git commit -a" ; "git checkout main" ; "git init" ; "git commit -a" ; "git merge lfs" ; "git lfs install" ; "git lfs track "*.bin"" ; "git add .attributes" ; "git add large_file.bin" ; "git commit -a" ; "git push origin main"


TASK 3--

step1- create a branch "geometry-calculator" and create a pyton file "geo_cal.py".      commands "git checkout -b geometry-calculator" and "touch geo_cal.py" after this add and commit the changes
step2- now use the "git log" command and copy the commit id
step3- create a new branch "feature/circle-area" and cherry pick the geo_cal.py file using commands- "git checkout -b feature/circle-area" and "git cherry-pick commitId"
step4- now write the code in for circlefeature in geo_cal.py and stash it in the middle of it by using command "git stash"
step5- create a new branch "feature/rectangle-area" and do the same things we did in the step3 and step4 by writing code for rectangle feature.
step6- now come back to "feature/circle-area" branch and by adding and commiting appply command "git stash apply"
step7- now write the full code for circle feature and the apply add and commit and checkout to "feature/rectangle-area" branch
step8- repeat the same step6 and step7 process for rectangle area and checkout to "geomerty-calculator" branch.
step9- now merge both "feature/circle_area" and "feature/rectangle_area" using "git merge" command and solve the merge conflicts by uniforming the code with help of "vi" command and then apply "git commmit -a" and "git checkout main" command to checkout to main command
step10- merge the "geomerty-calculator" branch to main branch and push the code to the git repository
