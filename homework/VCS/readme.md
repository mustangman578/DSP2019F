Problem Part 2.A
$ git branch test1 && git branch test2

Problem Part 2.B
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (master)
$ git checkout test1
Switched to branch 'test1'

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test1)
$ touch test.txt

Problem Part 2.C
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test1)
$ vi test.txt

Problem Part 2.D
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test1)
$ git add test.txt
warning: LF will be replaced by CRLF in homework/VCS/test.txt.
The file will have its original line endings in your working directory.

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test1)
$ git commit
[test1 99c4fe6]  On branch test1  Changes to be committed:      new file:   test.txt
 1 file changed, 1 insertion(+)
 create mode 100644 homework/VCS/test.txt

Problem Part 2.E
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test1)
$ git checkout test2
Switched to branch 'test2'

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ ls
readme.md

I don't see the file because it was specific to test1

Problem Part 2.F
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ touch test.txt

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ vi test.txt

Problem Part 2.G
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ git checkout test1
error: The following untracked working tree files would be overwritten by checkout:
        homework/VCS/test.txt
Please move or remove them before you switch branches.
Aborting

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ rm test.txt

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ git checkout test1
Switched to branch 'test1'

Problem Part 2.H
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ git checkout master
Switched to branch 'master'

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (master)
$ git merge test1
Updating 508995d..99c4fe6
Fast-forward
 homework/VCS/test.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 homework/VCS/test.txt

Problem Part 2.I
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (master)
$ ls
readme.md  test.txt

Problem Part 2.J
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (master)
$ git merge test2
Already up to date.

I don't get an error

Problem Part 2.K
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (master)
$ git checkout test2
Switched to branch 'test2'

I don't get an error

Problem Part 2.L
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ git status
On branch test2
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   .readme.md.swp

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   .readme.md.swp

Problem Part 2.M
The file was already removed

Problem Part 2.N
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ git status
On branch test2
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   .readme.md.swp

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   .readme.md.swp


Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ git commit
[test2 070e023]  On branch test2
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 homework/VCS/.readme.md.swp

Problem Part 2.O
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ git branch -d test1
error: The branch 'test1' is not fully merged.
If you are sure you want to delete it, run 'git branch -D test1'.

Problem Part 2.P
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ git checkout master
error: Your local changes to the following files would be overwritten by checkout:
        homework/VCS/.readme.md.swp
Please commit your changes or stash them before you switch branches.
Aborting

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ ls
readme.md

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ ls -la
total 20
drwxr-xr-x 1 Andrew 197608     0 Sep  9 13:32 ./
drwxr-xr-x 1 Andrew 197608     0 Sep  9 12:48 ../
-rw-r--r-- 1 Andrew 197608 16384 Sep  9 13:36 .readme.md.swp
-rw-r--r-- 1 Andrew 197608     0 Sep  9 12:49 readme.md

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ rm .readme.md.swp

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (master)
$ git branch -d test1
Deleted branch test1 (was 99c4fe6).

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (master)
$ git branch
* master
  test2

Problem Part 2.Q
I did not fully merge test1 when trying to delete it from test2.  Since I was on master, I could delete test1

Problem Part 2.R
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (master)
$ git checkout test2
Switched to branch 'test2'

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ git branch -d test2
error: Cannot delete branch 'test2' checked out at 'C:/Users/Andrew/DSP2019F'

Problem Part 2.S
Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (test2)
$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (master)
$ git branch -d test2
error: The branch 'test2' is not fully merged.
If you are sure you want to delete it, run 'git branch -D test2'.

Andrew@Andrew-PC MINGW64 ~/DSP2019F/homework/VCS (master)
$ git branch -D test2
Deleted branch test2 (was 070e023).




