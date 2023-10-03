
 KhobraPy Manual
 ==============================

 KhobraPy is intended as programming exercise.

 It consists in a very simple version of the classical 80s' arcade snake game
 written in Python, that is provided as an initial codebase  that should be 
 further extended by the learner. It was originally created as an educational
 resource to teach open-source development practices, tools and project
 management methodologies to graduate computer sciences students.

 KhobraPy is free software and can be distributed under the GNU General Public
 License vr.3 or any later version.

 The Game
 ------------------------------

 The game takes place on a rectangular arena where a snake continuously
 move in one of the four orthogonal directions: left, right, up and down;
 it never  stops. The challenge consists in steering the snake using the game
 controls to help it eat apples that are placed in random positions. Once
 consumed, apples appear elsewhere.

 Be careful, though. The arena borders are electrified and would kill the snake
 if touched. Moreover, mind that the snake is poisonous and it will also die if 
 it accidentally bites itself, i.e. if the snake's head crosses its own tail.

 The game score is the count of apples eaten until the game is over, and thus
 one should collect as many as possible.

 But there's a catch: the snake lengthens each time it eats an apple.
 
 CONTROLS

 * `arrow keys`:  move the snake up, down, left, right
 * `Q / q     `:  quits the game at any instant

 When the game ends, press any key to restart or 'q' to quit.

 Programming exercise
 ------------------------------

  The practice consists in

   a) fixing the listed known issues (bugs and requested features);
   
   b) improving the game by adding some awesome new features.

 Important information for developers can be found in the file
 `docs/CONTRIBUTING.md`. Please, **do read it** before starting your
 contribution.

 Known issues (that you should resolve)
 --------------------------------------

 KNOWN BUGS

 * The snake can reverse movement and bite-itself (e.g. if it's moving right and
   the player press the left key). There is a bug that causes the self-bite not
   to be detected if the tail has only one segment (reverse movement is an
   allowed move in the present version).

 * There is a small random chance that an apple be dropped onto the snake
   (trying to eat it is detected as self-bite). The probability is small but
   it increases as the snake lengthens.  

 REQUESTED FEATURES

 * In the traditional snake game, as the snake moves, it looses energy and,
   if all of it is exhausted, the snake dies. To restore energy, the snake
   needs to eat apples. The snake should be born with 100% energy level and
   gradually expend energy as it moves. An energy meter should be shown.

 * Before the game starts, the user might have the possibility of choosing
   some game parameters such as

	  * the size of the grid
	  * the snake speed
   	  * the number of apples in the arena. 
	  * whether reversing the snake is allowed or not
	  * whether apples disappear after some time
	  * whether there may be poisoned apples that degrades energy
	  * how much the snake grows by eating one apple

 * Before the game starts, the user should have the option of choosing
   the level of difficulty --- which might include some preset combinations
   of the former game parameters. Another possibility would be to choose
   whether the difficulty level increases as the score is raised.

 * The game should save the highest score.
  
 * The snake should start in a random position (but not too close to the
   border where it is heading to).

 Directions for this exercise
 ------------------------------

 The official repository of KhobraPy is https://github.com/monacofj/khobrapy.

 To start working on the exercise:

 * fork this project using the functionality of the hosting platform;

 * give the development team access to the forked repository;
 
 * follow the instructions given in `docs/CONTRIBUTING.md`.

 __VERY IMPORTANT__

 Bear in mind that you will be creating a new game. It will be based on
 KhobraPy but will be another software. Therefore you will be starting
 a new project (rather tan contributing to this one).

 Begin so, you **will have to** document your project properly, what includes
 rewriting files such as `README.md`, `manual.md`, `AUTHORS` and possibly
 `CONTRIBUTING.md` with your project's information.

 Also, you **must** edit the author and copyright information in every source
 file accordingly (see e.g. the heading comments at the top of khobra.py)

 Finally, every open-open source project naturally deserves a cool, catchy,
 amazing name. (KhobraPy is out of question). Choose one and rename your
 repository accordingly.

 Happy coding.