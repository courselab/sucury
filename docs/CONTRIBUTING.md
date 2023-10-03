
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
 
 ### Commit types
 
 Select the appropriate type.
 
 - fix:   fix a bug
 - feat:  add new feature
 - build: changes affecting the build 
 - perf:  tidy code (other than the above) and repository
 - doc:   modify internal or external documentation
 - test:  add or modify tests
 - tmp:   a temporary branch for some other purpose (not PR/MR)

 Examples

 * your PR/MR will fix the bug pointed out by issue #42 that
   crashes the program:

   `fix/#42/stop-crashing`

 * your PR/MR will add the featured described by issue #142 that
   adds a debug mode option:

   `feat/#142/debug-option`

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

 ### How to comment

  Make it easier for newcomers to join in: comment generously (considerately,
  not recklessly.) You may have heard that "good code documents itself" and
  yes, using descriptive variables and function names frees you from the
  need to explain what they are meant for. Yet, when it comes to the free
  open-source ecosystem, one should be mindful of the novice contributors
  who may save precious time by reading some courtesy notes. In special,
  it's advisable to offer hints about the purpose of each piece of code,
  even if that can be inferred from reading source --- bear in mind that
  some rookie developers may be contributing to learn programming skills.

 ### Code of conduct

 * Be respectful and welcoming to diversity.
 * Do not engage in raging arguments.

 ### Repository management

 Latest stable releases resides in the `main` branch.

 Prerelease (alpha, beta, release candidates) reside in branch `prerelease`.

 If you are a developer and is assigned an issue, but you believe you are not
 able to handle it timely, please, try to reassign it to someone else.

 ChangeLog should be kept up-to-date; NEWS should be updated upon (pre)releases.

 It should be needless to say, but do not commit unnecessary files (e.g. files
 that can be produced during the build process (if any).

 ## References

 [1] https://nvie.com/posts/a-successful-git-branching-model/

 [2] https://semver.org/

 [3] https://www.conventionalcommits.org/en/v1.0.0/

 [4] https://keepachangelog.com/en/1.0.0/

 [5] https://peps.python.org/pep-0008/