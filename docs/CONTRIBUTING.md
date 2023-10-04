
 Contributing to this project
 ==============================

 Before starting to contribute, please read these directions thoroughly.

 Essential notes
 ------------------------------
 
 To keep things consistent, we adhere to some standards

 - GitFlow branching strategy [1] (plus a prerelease branch)

 - Semantic versioning 2.0.0 [2]

 - Conventional Commits 1.0.0 [3] (see types bellow)

 - Keep a ChangeLog [4]

 - Python coding convention [5]
 
### Submitting contributions

 First create and issue for your contribution, if one does not exist yet.
 
 Develop your contribution in a support branch, following the naming scheme
 
 `type/issue-number/short-descriptive-annotation`

 where `type` is a conventional commit type (see below).
 
 Submit your support branch and mark it as a pull/merge request.
 
 ### Commit messges

 When writing a commit message, use the following template --- which is 
 furhter described in [3]

 ```
 <type>[optional scope]: <short description of what the commit does>

 [optional body with further deails]

 [optional footers]

 ```
 where `type` is one of the following conventional commit types:

 - `fix`:   fix a bug
 - `feat`:  add new feature
 - `build`: changes affecting the build 
 - `perf`:  tidy code (other than the above) and repository
 - `doc`:   modify internal or external documentation
 - `test`:  add or modify tests
 - `tmp`:   a temporary branch for some other purpose (not PR/MR)

 If one realizes that one commit serves multiple purposes, that suggests that
 the commit might be split into two or more single-purpose commits.

 Refer to [3] for the rationales of conventional commits.

 ### Branch names

 When naming an ephemeral branch, indicate its purpose by choosing among
 `feature`, `bugfix`, `hotfix`, `release`, `wip`, or `exp`, abiding by the
 following convention.

 __Branch related to an issue__

 `<purpose>/<issue number>/<short-descriptive-mnemonic>`

 where `purpose` is one of the following:

 * `feature`:   adding, modifying or removing a feature
 * `bugfix`:    fixes a bug in the development branch
 * `hotfix`:    fixes a but in the public (main) branch
 * `wip`   :    work-in-progress (to be converted when done)

 Use lowercase kebab-case for the `short-descriptive-mnemonic`.
 
 __Release branch__

 `release/<release number>`

  where `release number` is the SemVer naming of the release preceded by 'v'.

 __Experimental branch___

 To experiment with something not related to an issue, use

 `exp/<short-descriptive-mnemonic>`

Examples

 * your PR/MR will fix the bug pointed out by issue #42 that
   crashes the program:

   `bugfix/42/divide-by-zero`

 * your PR/MR will add the featured described by issue #142 that
   adds a debug mode option:

   `featuer/142/debug-option`

 * your PR/MR is meant to prepare the release 1.0.1

   `release/v1.0.1`

 ### Code standards

  When contributing to an open-source project, it's a good practice to
  abide by to coding standards of the community.

  For this practice, follow [5], with these highlights:

  * functions, variables, methods and modules: `snake_case`
  * classes: `PascalCase`
  * constants: `CAPITALIZED_SAKE_CASE`

  Also, in this project, we're following the following guidelines.

  * Code and comment in English as a lingua franca (you can have more
    people understanding you with bad English than with erudite Latin). 

  * Comments are regular text. Capitalize and punctuate accordingly.
    Write "This function does this and that."; not "this function 
    does this and that" if that is the whole sentence.

 ### What to comment

  Make it easier for newcomers to join in: comment generously (considerately,
  not recklessly.) You may have heard that "good code documents itself" and
  yes, using descriptive variables and function names frees you from the
  need to explain what they are meant for. Yet, when it comes to the free
  open-source ecosystem, one should be mindful of the novice contributors
  who may save precious time by reading some courtesy notes. In special,
  it's advisable to offer hints about the purpose of each piece of code,
  even if that can be inferred from reading source --- bear in mind that
  some rookie developers may be contributing to learn programming skills.


 ### Repository policy

 * Stable releases reside in the `main` branch.

 * Prereleases (alpha, beta etc.) reside in branch `prerelease`.

 * When integrating ephemeral branches into permanent branches (GitFlow),
   use merge, not rebase. It is ok, however, to thoughtfully squash selected
   commits via interactive rebase before merging to highlight relevant
   changes in the development history.

 * Label your issues and, if there is an issue template, use it as well.

 * If you are a developer and is assigned an issue, but you believe you are
   not able to handle it timely, please, try to reassign it to someone else.

 * File `ChangeLog` contains technical notes describing the notable changes
   that interest the developers. It should be updated, if applicable, every
   time the `develop` branch is modified.
   
 * File `NEWS` contains the release notes that interest the final user. It
   should be updated upon every  public (pre)release.

 * File `AUTHORS` lists all those who have contributed to the project (if
   full names are not know, include e-mail or the username that the contributor
   uses in the SCM platform (e.g. GitHub, GitLab), ensuring that the URL of
   the project is also informed. This file should be kept updated.

 It should be needless to say, but do not commit unnecessary files (e.g. files
 that can be produced during the build process (if any).

 ### Code of conduct

 * Be respectful and welcoming to diversity.
 
 * Do not engage in raging arguments.

 ## References

 [1] https://nvie.com/posts/a-successful-git-branching-model/

 [2] https://semver.org/

 [3] https://www.conventionalcommits.org/en/v1.0.0/

 [4] https://keepachangelog.com/en/1.0.0/

 [5] https://peps.python.org/pep-0008/