# SoftwareEngineering
Algorithm and Data Structure

Cloud IDE : https://replit.com/ 

Referlink: https://www.nsnam.org/


# Additional Tools

https://arp242.net/diy.html 

https://help.github.com/en/articles/closing-issues-using-keywords

https://help.github.com/en/articles/setting-guidelines-for-repository-contributors 

https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html

https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/

https://docs.travis-ci.com/user/tutorial/

https://docs.travis-ci.com/user/build-stages/


# Advanced Git Cheat Sheet
<table>
  <tr>
    <th>Command</th>
    <th>Explanation & Link</th>
  </tr>
  <tr>
    <td>git commit -a</td>
    <td>Stages files automatically</td>
  </tr>
  <tr>
    <td>git log -p</td>
    <td>Produces patch text</td>
  </tr>
  <tr>
    <td>git show</td>
    <td>Shows various objects</td>
  </tr>
  <tr>
    <td>git diff</td>
    <td>Is similar to the Linux `diff` command, and can show the differences in various commits</td>
  </tr>
  <tr>
    <td>git diff --staged</td>
    <td>An alias to --cached, this will show all staged files compared to the named commit</td>
  </tr>
  <tr>
    <td>git add -p</td>
    <td>Allows a user to interactively review patches to add to the current commit</td>
  </tr>
  <tr>
    <td>git mv</td>
    <td>Similar to the Linux `mv` command, this moves a file</td>
  </tr>
  <tr>
    <td>git rm</td>
    <td>Similar to the Linux `rm` command, this deletes, or removes a file</td>
  </tr>

</table>


There are many useful git cheatsheets online as well. Please take some time to research and study a few, such as this one.

.gitignore files
.gitignore files are used to tell the git tool to intentionally ignore some files in a given Git repository. For example, this can be useful for configuration files or metadata files that a user may not want to check into the master branch. Check out more at: https://git-scm.com/docs/gitignore.

A few common examples of file patterns to exclude can be found here.

# Git Revert Cheat Sheet

git checkout(https://git-scm.com/docs/git-checkout) is effectively used to switch branches.
 
git reset(https://git-scm.com/docs/git-reset#_examples) basically resets the repo, throwing away some changes. It’s somewhat difficult to understand, so reading the examples in the documentation may be a bit more useful.t

There are some other useful articles online, which discuss more aggressive approaches to resetting the repo(https://jwiegley.github.io/git-from-the-bottom-up/3-Reset/4-doing-a-hard-reset.html).

git commit --amend(https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend) is used to make changes to commits after-the-fact, which can be useful for making notes about a given commit.

git revert(https://git-scm.com/docs/git-revert) makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.

There are a few ways(https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) you can rollback commits in Git.

There are some interesting considerations about how git object data is stored, such as the usage of sha-1. 

Feel free to read more here:

https://en.wikipedia.org/wiki/SHA-1

https://github.blog/2017-03-20-sha-1-collision-detection-on-github-com/


# Git Branches and Merging Cheat Sheet

<table>
  <tr>
    <th>Command</th>
    <th>Explanation & Link</th>
  </tr>
  <tr>
    <td>git branch</td>
    <td>Used to manage branches</td>
  </tr>
  <tr>
    <td>git branch <name></td>
    <td>Creates the branch</td>
  </tr>
  <tr>
    <td>git branch -d <name></td>
    <td>Deletes the branch</td>
  </tr>
  <tr>
    <td>git branch -D <name></td>
    <td>Forcibly deletes the branch</td>
  </tr>
  <tr>
    <td>git checkout <branch></td>
    <td>Switches to a branch.</td>
  </tr>
  <tr>
    <td>git checkout -b <branch></td>
    <td>Creates a new branch and switches to it.</td>
  </tr>
  <tr>
    <td>git merge <branch> </td>
    <td>Merge joins branches together. </td>
  </tr>
  <tr>
    <td>git merge --abort</td>
    <td>If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action.</td>
  </tr>
  <tr>
    <td>git log --graph --oneline</td>
    <td>This shows a summarized view of the commit history for a repo.</td>
  </tr>
</table>


# Git Remotes Cheat-Sheet

<table>
  <tr>
    <th>Command</th>
    <th>Explanation & Link</th>
  </tr>
  <tr>
    <td>git remote</td>
    <td>Lists remote repos(https://git-scm.com/docs/git-remote)</td>
  </tr>
  <tr>
    <td>git remote -v</td>
    <td>List remote repos verbosely(https://git-scm.com/docs/git-remote#Documentation/git-remote.txt--v)</td>
  </tr>
  <tr>
    <td>git remote show <name></td>
    <td>Describes a single remote repo(https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emshowem)</td>
  </tr>
  <tr>
    <td>git remote update</td>
    <td>Fetches the most up-to-date objects(https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emupdateem)</td>
  </tr>
  <tr>
    <td>git fetch</td>
    <td>Downloads specific objects(https://git-scm.com/docs/git-fetch)</td>
  </tr>
  <tr>
    <td>git branch -r</td>
    <td>Lists remote branches; can be combined with other branch arguments to manage remote branches (https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--r)</td>
  </tr>
</table>


# Google Python Style Guide
More Information on Code Reviews
http://google.github.io/styleguide/

https://help.github.com/en/articles/about-pull-request-reviews

https://medium.com/osedea/the-perfect-code-review-process-845e6ba5c31

https://smartbear.com/learn/code-review/what-is-code-review/
