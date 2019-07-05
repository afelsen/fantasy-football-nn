# Fantasy Football Neural Network
#### Created by Adiel Felsen

## Description
This neural network predicts [fantasy football](https://en.wikipedia.org/wiki/Fantasy_football_(American)) scores (standard scoring) for the quarterback (QB), running back (RB), wide receiver (WR) and tight end (TE) positions.

## Resources
* This program uses [keras](https://keras.io/) to constuct the neural network
* [numpy](https://www.numpy.org/), [scipy](https://www.scipy.org/) and [pandas](https://pandas.pydata.org/) are used to structure the data
* [matplotlib](https://matplotlib.org/) is used to plot the results
* All data is sourced from [Pro Football Reference](https://www.pro-football-reference.com/)

## Neural Network Training


#### Training Data ####

The training data is the statistics of each NFL player (in the relevant position) from 1980 to 2016 and is sourced from pro-football-reference.com
* These statistics include: Rank (Since 1980), Year, Age, Games Played, Games Started, FantPt (standard), FantPt (PPR), FantPt/G (standard), FantPt/G (PPR), Cmp, P-Att, P-Yds, P-TD, Int, Ru-Att, Ru-Yds, Ru-TD, Rec, Rec-Yds, Rec-TD, Fmb
* Each player's career statistics is divided to generate more training data
  * For example, if a player played from 1990 - 1992, his statistics would be represented as three data points: 1990, 1990-1991 and 1990-1992
* Each data point is padded with zeros to make its shape (22,22)

#### Structure and Training ####

All positions are trained with the same sequential network structure:
* Two convolutional layers (filters = 22 and 10 respectively)
* A flatten layer
* Two dense layers (filters = 64 and 1 respectively)

For the current models (in Models folder) the epochs vary to account for different training data sizes:
* QB position is trained for 300 epochs
* TE position is trained for 200 epochs
* WR and RB positions are trained for 150 epochs


## Neural Network Testing

The neural network is tested with 2017 player data and 2018 labels. Data for the ESPN comparisons are from the [ESPN Fantasy Football Draft Kit](https://g.espncdn.com/s/ffldraftkit/18/NFLDK2018_CS_PPR300.pdf). The results for each model is as follows:
* QB Model

   * Average Ranking Difference: 10.81
      * (Average Ranking Difference ESPN: 7.14)
   * Median Ranking Difference: 7.5
      * (Median Ranking Difference ESPN: 7.0)
   * Average Score Difference: 75.32
   * Median Score Difference: 60.54

* RB Model
   * Average Ranking Difference: 25.82
      * (Average Ranking Difference ESPN: 17.51)
   * Median Ranking Difference: 22.5
      * (Median Ranking Difference ESPN: 15.0)
   * Average Score Difference: 51.21
   * Median Score Difference: 39.09

* WR Model
   * Average Ranking Difference: 28.59
      * (Average Ranking Difference ESPN: 19.07)
   * Median Ranking Difference: 24.0
      * (Median Ranking Difference ESPN: 17.5)
   * Average Score Difference: 43.88
   * Median Score Difference: 34.15

* TE Model
  * Average Ranking Difference: 17.82
      * (Average Ranking Difference ESPN: 8.91)
  * Median Ranking Difference: 13.0
      * (Median Ranking Difference ESPN: 5.0)
  * Average Score Difference: 27.07
  * Median Score Difference: 17.48


## Predictions

Predictions are based on 2018 data. Predictions do not include any players who were not in the NFL in 2018. Predictions also do not take into account current events (such as retirement, injury or trades).

#### QB Model

| 1. Tom Brady: 447.78 |2. Cam Newton: 385.05 |3. Nick Mullens: 334.39 |4. Deshaun Watson: 328.59 |5. Baker Mayfield: 327.93 |
|---|---|---|---|---|
| 6. Matt Ryan: 326.57 |7. Drew Brees: 312.18 |8. Aaron Rodgers: 305.21 |9. Russell Wilson: 303.53 |10. Jameis Winston: 297.53 |
| 11. Andrew Luck: 296.46 |12. Lamar Jackson: 287.25 |13. Ben Roethlisberger: 286.06 |14. Andy Dalton: 279.34 |15. Mitchell Trubisky: 268.95 |
| 16. Philip Rivers: 266.37 |17. Kirk Cousins: 265.39 |18. Eli Manning: 251.18 |19. Derek Carr: 225.97 |20. Ryan Fitzpatrick: 225.95 |
| 21. Matthew Stafford: 220.65 |22. Jared Goff: 220.65 |23. Joe Flacco: 215.46 |24. Sam Darnold: 204.93 |25. Brock Osweiler: 204.42 |
| 26. Tyrod Taylor: 159.44 |27. Case Keenum: 154.57 |28. Brian Hoyer: 153.11 |29. Marcus Mariota: 152.78 |30. Carson Wentz: 147.46 |
| 31. Jeff Driskel: 143.53 |32. Jimmy Garoppolo: 138.88 |33. Patrick Mahomes: 135.86 |34. Blaine Gabbert: 134.16 |35. C.J. Beathard: 129.49 |
| 36. Josh Rosen: 124.54 |37. Alex Smith: 117.52 |38. Dak Prescott: 116.75 |39. Josh Johnson: 107.95 |40. Blake Bortles: 107.95 |
| 41. Kyle Lauletta: 103.49 |42. Derek Anderson: 98.12 |43. Ryan Tannehill: 96.91 |44. Kyle Allen: 90.42 |45. Josh Allen: 81.24 |
| 46. Nate Sudfeld: 78.41 |47. Matt Schaub: 70.24 |48. Mark Sanchez: 69.44 |49. Matt Cassel: 68.92 |50. Josh McCown: 68.91 |
| 51. Sam Bradford: 67.89 |52. Sean Mannion: 66.23 |53. A.J. McCarron: 59.18 |54. Terrelle Pryor: 55.6 |55. Garrett Gilbert: 52.4 |
| 56. Nathan Peterman: 49.4 |57. Cooper Rush: 44.06 |58. Teddy Bridgewater: 43.81 |59. Geno Smith: 36.79 |60. Joshua Dobbs: 35.7 |
| 61. Nick Foles: 33.11 |62. Cody Kessler: 31.61 |63. Chad Kelly: 31.53 |64. Taylor Heinicke: 27.85 |65. Robert Griffin: 25.16 |
| 66. Brandon Weeden: 22.41 |67. Taysom Hill: 18.09 |68. DeShone Kizer: 6.63 |69. Chase Daniel: 5.38 |70. Joe Webb: 0.38 |
| 71. Mike Glennon: -30.57 |72. Colt McCoy: -36.59 |73. Chad Henne: -37.36 |74. Jacoby Brissett: -59.87 |75. Matt Barkley: -77.1 |

#### RB Model

| 1. Frank Gore: 431.41 |2. Melvin Gordon: 349.33 |3. James Conner: 345.88 |4. Alvin Kamara: 239.34 |5. Todd Gurley: 225.7 |
|---|---|---|---|---|
| 6. Ezekiel Elliott: 214.83 |7. Spencer Ware: 210.31 |8. Kareem Hunt: 205.62 |9. James White: 204.63 |10. Mark Ingram: 192.95 |
| 11. Leonard Fournette: 190.35 |12. Tevin Coleman: 189.85 |13. Joe Mixon: 188.47 |14. Marlon Mack: 181.27 |15. David Johnson: 178.81 |
| 16. Saquon Barkley: 173.37 |17. Kerryon Johnson: 172.36 |18. Devonta Freeman: 165.32 |19. Jay Ajayi: 161.0 |20. Tarik Cohen: 160.99 |
| 21. Jordan Howard: 160.74 |22. T.J. Yeldon: 159.01 |23. Aaron Jones: 157.87 |24. Matt Breida: 155.04 |25. Chris Thompson: 150.89 |
| 26. Giovani Bernard: 149.76 |27. Doug Martin: 148.28 |28. Christian McCaffrey: 146.48 |29. Alex Collins: 139.45 |30. Lamar Miller: 130.19 |
| 31. LeGarrette Blount: 129.74 |32. Stevan Ridley: 129.5 |33. Phillip Lindsay: 129.4 |34. Theo Riddick: 128.53 |35. Jamaal Williams: 128.25 |
| 36. Isaiah Crowell: 124.76 |37. Peyton Barber: 123.08 |38. C.J. Anderson: 121.02 |39. Duke Johnson: 113.21 |40. Jeremy Langford: 111.86 |
| 41. Jalen Richard: 111.19 |42. Sony Michel: 110.96 |43. Rashaad Penny: 110.83 |44. Latavius Murray: 110.46 |45. Chris Ivory: 106.39 |
| 46. Carlos Hyde: 98.43 |47. Alfred Morris: 93.66 |48. Kenyan Drake: 90.66 |49. Jordan Wilkins: 89.3 |50. Austin Ekeler: 87.96 |
| 51. Jeremy Hill: 87.2 |52. Nick Chubb: 84.55 |53. Josh Adams: 83.31 |54. Gus Edwards: 81.81 |55. Benny Cunningham: 79.26 |
| 56. LeSean McCoy: 76.71 |57. Samaje Perine: 75.61 |58. Ito Smith: 75.24 |59. Bilal Powell: 73.55 |60. Mike Gillislee: 72.05 |
| 61. Kalen Ballage: 71.57 |62. Nyheim Hines: 71.24 |63. Justin Jackson: 71.18 |64. Royce Freeman: 70.49 |65. Ameer Abdullah: 69.01 |
| 66. Dalvin Cook: 69.0 |67. Dion Lewis: 68.41 |68. Chris Carson: 67.85 |69. Jeff Wilson: 66.53 |70. Jaylen Samuels: 65.57 |
| 71. Derrick Henry: 65.21 |72. Malcolm Brown: 62.96 |73. Corey Grant: 59.75 |74. Kyle Juszczyk: 59.58 |75. Jonathan Stewart: 58.87 |
| 76. Charcandrick West: 58.7 |77. Alfred Blue: 58.1 |78. Corey Clement: 56.77 |79. John Kelly: 54.81 |80. Brandon Bolden: 51.97 |
| 81. Marshawn Lynch: 50.23 |82. Wayne Gallman: 50.01 |83. Chase Edmonds: 47.84 |84. Jamaal Charles: 47.56 |85. David Fluellen: 47.27 |
| 86. Devontae Booker: 44.81 |87. Adrian Peterson: 44.35 |88. Darrel Williams: 43.97 |89. Brian Hill: 43.96 |90. Andy Janovich: 40.93 |
| 91. Trenton Cannon: 40.17 |92. Justin Davis: 38.11 |93. Taquan Mizzell: 37.71 |94. Elijah McGuire: 35.08 |95. Wendell Smallwood: 33.51 |
| 96. Roc Thomas: 32.04 |97. Mark Walton: 31.22 |98. Kenneth Dixon: 31.13 |99. Mike Boone: 30.6 |100. Derrick Coleman: 30.48 |
| 101. Ronald Jones: 29.32 |102. Senorise Perry: 29.28 |103. Derek Watt: 28.47 |104. Mike Davis: 28.08 |105. David Williams: 27.9 |
| 106. Christine Michael: 27.47 |107. Detrez Newsome: 26.63 |108. Tre Madden: 26.44 |109. Robert Turbin: 26.33 |110. Javorius Allen: 25.9 |
| 111. Keith Smith: 24.76 |112. Zach Zenner: 24.46 |113. Darius Jackson: 24.38 |114. Danny Vitale: 24.17 |115. Dwayne Washington: 23.88 |
| 116. Damien Williams: 23.67 |117. C.J. Ham: 22.82 |118. Rod Smith: 21.95 |119. Travaris Cadet: 21.67 |120. Shaun Wilson: 21.47 |
| 121. Zach Line: 20.56 |122. Elijhaa Penny: 20.06 |123. Keith Ford: 19.96 |124. De'Lance Turner: 19.77 |125. Byron Marshall: 19.49 |
| 126. Patrick DiMarco: 18.96 |127. Gregory Howell: 17.26 |128. Dontrell Hilliard: 16.59 |129. Tra Carson: 15.88 |130. Patrick Ricard: 15.56 |
| 131. Buddy Howell: 15.31 |132. Dalyn Dawkins: 15.05 |133. Lavon Coleman: 15.01 |134. Boston Scott: 14.32 |135. Keenan Reynolds: 14.21 |
| 136. Ricky Ortiz: 13.61 |137. Brandon Wilds: 13.4 |138. Alex Armah: 13.31 |139. Jeremy McNichols: 12.38 |140. Nick Bellore: 12.18 |
| 141. C.J. Prosise: 11.58 |142. T.J. Logan: 9.81 |143. Matthew Dayes: 9.52 |144. Michael Burton: 8.65 |145. Anthony Sherman: 8.5 |
| 146. Jacquizz Rodgers: 8.32 |147. Tyler Ervin: 7.92 |148. Tommy Bohanon: 7.79 |149. Jonathan Williams: 7.64 |150. Trey Edmunds: 5.49 |
| 151. Kenjon Barner: 5.32 |152. DeAndre Washington: 3.55 |153. Jamize Olawale: 3.16 |154. De'Angelo Henderson: 2.7 |155. Roosevelt Nix: 2.35 |
| 156. Marcus Murphy: -1.94 |157. Dare Ogunbowale: -2.83 |158. Shane Smith: -4.98 |159. Raheem Mostert: -7.03 |160. Cameron Artis-Payne: -9.86 |
| 161. Kapri Bibbs: -12.94 |162. James Develin: -29.35 |163. Robert Kelley: -71.78 |164. D'Onta Foreman: -76.59 |165. Thomas Rawls: -116.46 |

#### WR Model

| 1. Odell Beckham: 252.14 |2. Antonio Brown: 230.29 |3. JuJu Smith-Schuster: 223.48 |4. Josh Gordon: 211.66 |5. Michael Thomas: 191.48 |
|---|---|---|---|---|
| 6. Keenan Allen: 172.18 |7. Davante Adams: 172.18 |8. Dede Westbrook: 169.1 |9. Kenny Golladay: 168.43 |10. Adam Thielen: 166.6 |
| 11. Mohamed Sanu: 163.02 |12. Amari Cooper: 161.8 |13. Julian Edelman: 160.66 |14. Robert Woods: 160.23 |15. Doug Baldwin: 147.07 |
| 16. Chris Godwin: 145.35 |17. Justin Hardy: 142.18 |18. A.J. Green: 141.43 |19. DeAndre Hopkins: 141.22 |20. Demaryius Thomas: 140.11 |
| 21. Tyreek Hill: 139.01 |22. Sterling Shepard: 137.52 |23. Trent Taylor: 133.88 |24. Seth Roberts: 133.63 |25. Cooper Kupp: 132.43 |
| 26. Pierre Garcon: 132.13 |27. Sammy Watkins: 130.42 |28. Tyrell Williams: 128.55 |29. Ryan Switzer: 128.43 |30. Jordy Nelson: 127.14 |
| 31. Willie Snead: 124.96 |32. Brandin Cooks: 124.82 |33. Christian Kirk: 124.53 |34. Adam Humphries: 123.07 |35. Stefon Diggs: 122.51 |
| 36. Courtland Sutton: 121.5 |37. Calvin Ridley: 120.73 |38. Antonio Callaway: 116.52 |39. Rod Streater: 116.52 |40. Larry Fitzgerald: 114.39 |
| 41. Jarvis Landry: 114.27 |42. Tajae Sharpe: 109.44 |43. Robby Anderson: 109.17 |44. Chester Rogers: 108.78 |45. DeSean Jackson: 107.55 |
| 46. Emmanuel Sanders: 107.09 |47. Allen Robinson: 105.66 |48. T.Y. Hilton: 105.19 |49. Maurice Harris: 105.05 |50. Mike Evans: 103.14 |
| 51. Keelan Cole: 102.27 |52. Marquez Valdes-Scantling: 101.61 |53. Michael Floyd: 100.42 |54. David Moore: 98.47 |55. Julio Jones: 98.07 |
| 56. Alshon Jeffery: 97.39 |57. Allen Hurns: 94.13 |58. Darius Jennings: 92.64 |59. Torrey Smith: 92.2 |60. Michael Gallup: 92.0 |
| 61. Dante Pettis: 91.8 |62. Jamison Crowder: 91.0 |63. Jordan Matthews: 90.08 |64. Corey Davis: 88.87 |65. Chris Moore: 86.89 |
| 66. Trey Quinn: 86.59 |67. Eli Rogers: 85.89 |68. Zay Jones: 85.83 |69. Jermaine Kearse: 84.15 |70. Dontrelle Inman: 83.22 |
| 71. Corey Coleman: 82.74 |72. Mike Wallace: 82.51 |73. Taylor Gabriel: 81.48 |74. Aldrick Robinson: 81.43 |75. Devin Funchess: 80.96 |
| 76. Quincy Enunwa: 80.22 |77. Robert Foster: 79.27 |78. Michael Crabtree: 79.26 |79. Kenny Stills: 78.45 |80. Randall Cobb: 78.43 |
| 81. Equanimeous St. Brown: 78.38 |82. Terrance Williams: 78.05 |83. Anthony Miller: 76.57 |84. Tre'Quan Smith: 75.93 |85. Tyler Lockett: 75.13 |
| 86. Jakeem Grant: 75.04 |87. Mike Williams: 74.8 |88. Jarius Wright: 74.79 |89. Curtis Samuel: 74.52 |90. Kendrick Bourne: 74.35 |
| 91. Rashard Higgins: 73.78 |92. Nelson Agholor: 73.28 |93. Kelvin Benjamin: 73.22 |94. Tyler Boyd: 70.82 |95. Josh Malone: 70.43 |
| 96. Phillip Dorsett: 68.13 |97. Bennie Fowler: 67.27 |98. D.J. Moore: 67.21 |99. Josh Reynolds: 66.56 |100. Travis Benjamin: 65.77 |
| 101. Brice Butler: 64.26 |102. Marvin Hall: 60.84 |103. Danny Amendola: 60.7 |104. Markus Wheaton: 60.11 |105. Ryan Grant: 59.59 |
| 106. Josh Bellamy: 58.64 |107. Martavis Bryant: 58.3 |108. Cordarrelle Patterson: 57.09 |109. Jehu Chesson: 56.27 |110. Chad Williams: 56.15 |
| 111. Russell Shepard: 55.53 |112. John Brown: 55.34 |113. Chris Conley: 54.22 |114. Tim Patrick: 52.93 |115. T.J. Jones: 52.64 |
| 116. Chris Hogan: 51.46 |117. Donte Moncrief: 51.23 |118. Sammie Coates: 49.66 |119. Andre Roberts: 49.26 |120. Leonte Carroo: 48.21 |
| 121. Rashad Greene: 47.77 |122. DJ Chark: 47.28 |123. Taywan Taylor: 46.91 |124. Nick Williams: 46.9 |125. Dwayne Harris: 46.72 |
| 126. Marvin Jones: 45.49 |127. James Washington: 44.99 |128. Ray-Ray McCloud: 44.87 |129. Trent Sherfield: 43.31 |130. Damiere Byrd: 42.53 |
| 131. Keith Kirkwood: 41.9 |132. Jaron Brown: 41.57 |133. Darrius Heyward-Bey: 40.63 |134. Andy Jones: 40.59 |135. Richie James: 39.2 |
| 136. Kevin White: 38.9 |137. Zach Pascal: 37.46 |138. Jalen Tolliver: 37.45 |139. Austin Carr: 36.71 |140. Chad Beebe: 36.71 |
| 141. Demarcus Robinson: 36.11 |142. DeVante Parker: 33.81 |143. Russell Gage: 33.49 |144. DaeSean Hamilton: 33.42 |145. Pharoh Cooper: 32.65 |
| 146. Geremy Davis: 32.58 |147. Josh Doctson: 32.45 |148. Cameron Batson: 32.09 |149. Damion Ratley: 31.94 |150. J.D. McKissic: 30.87 |
| 151. Saeed Blacknall: 30.34 |152. Deante Burton: 30.05 |153. Cole Beasley: 29.67 |154. Mike Thomas: 29.35 |155. Steven Dunbar: 28.83 |
| 156. Malachi Dupre: 28.79 |157. Trevor Davis: 28.76 |158. Isaiah Ford: 28.56 |159. Daurice Fountain: 28.51 |160. Rico Gafford: 28.44 |
| 161. Charone Peake: 27.76 |162. Tony Lippett: 27.58 |163. Noah Brown: 27.36 |164. Alonzo Russell: 27.34 |165. Max McCaffrey: 27.34 |
| 166. Steven Mitchell: 27.33 |167. Chris Lacy: 27.31 |168. Cam Sims: 27.22 |169. Da'Mari Scott: 27.08 |170. Marquise Goodwin: 26.48 |
| 171. Johnny Holton: 25.92 |172. Alex Erickson: 25.33 |173. Stacy Coley: 25.29 |174. Tanner McEvoy: 24.71 |175. Andre Holmes: 24.07 |
| 176. KhaDarel Hodge: 22.35 |177. Brandon Zylstra: 22.0 |178. Janarion Grant: 21.87 |179. John Ross: 21.21 |180. Keon Hatcher: 20.98 |
| 181. Riley McCarron: 20.84 |182. Cody Core: 20.59 |183. Justin Watson: 20.14 |184. Darvin Kidsy: 19.65 |185. Cam Phillips: 19.17 |
| 186. Tim White: 18.9 |187. Shelton Gibson: 18.25 |188. J'Mon Moore: 18.0 |189. Allen Lazard: 16.75 |190. Kaelin Clay: 15.3 |
| 191. River Cracraft: 14.03 |192. JJ Nelson: 10.22 |193. JJ Jones: 9.99 |194. Victor Bolden: 7.77 |195. Mose Frazier: 6.45 |
| 196. Jojo Natson: 0.81 |197. Laquon Treadwell: -1.28 |198. C.J. Goodwin: -2.0 |199. Marcus Kemp: -4.86 |200. Bradley Marquez: -6.03 |
| 201. Breshad Perriman: -14.01 |202. Matthew Slater: -15.92 |203. Brandon Tate: -20.0 | | |

#### TE Model

| 1. George Kittle: 141.81 |2. Rob Gronkowski: 131.5 |3. Eric Ebron: 117.61 |4. Zach Ertz: 104.06 |5. Mark Andrews: 96.04 |
|---|---|---|---|---|
| 6. Delanie Walker: 95.39 |7. Antonio Gates: 92.47 |8. David Njoku: 91.76 |9. Evan Engram: 90.53 |10. Charles Clay: 90.2 |
| 11. Chris Herndon: 87.41 |12. O.J. Howard: 86.08 |13. Austin Hooper: 85.37 |14. Jordan Reed: 82.21 |15. Greg Olsen: 80.12 |
| 16. Josh Hill: 70.21 |17. Dallas Goedert: 69.36 |18. Blake Jarwin: 64.46 |19. Kyle Rudolph: 64.34 |20. Cameron Brate: 63.61 |
| 21. Ben Watson: 63.3 |22. C.J. Uzomah: 60.93 |23. Jimmy Graham: 60.76 |24. Jordan Thomas: 56.26 |25. Ryan Griffin: 55.98 |
| 26. Travis Kelce: 54.99 |27. Gerald Everett: 51.21 |28. Vernon Davis: 50.85 |29. Anthony Firkser: 50.09 |30. Jesse James: 49.63 |
| 31. Ian Thomas: 49.29 |32. Dan Arnold: 45.4 |33. Mo Alie-Cox: 43.73 |34. Geoff Swaim: 42.51 |35. Matt LaCosse: 42.23 |
| 36. Nick Boyle: 41.73 |37. Jeff Heuerman: 40.82 |38. Trey Burton: 40.28 |39. Daniel Brown: 40.03 |40. Hayden Hurst: 37.97 |
| 41. Jared Cook: 37.07 |42. Nick Vannett: 36.14 |43. Jason Croom: 35.88 |44. Dwayne Allen: 34.28 |45. Demetrius Harris: 33.94 |
| 46. Jonnu Smith: 33.68 |47. James O'Shaughnessy: 33.39 |48. Ricky Seals-Jones: 32.24 |49. Nick O'Leary: 31.66 |50. Rhett Ellison: 31.22 |
| 51. Darren Fells: 29.57 |52. Logan Thomas: 29.49 |53. Luke Willson: 28.25 |54. Tyler Higbee: 27.96 |55. Robert Tonyan: 27.26 |
| 56. Jordan Leggett: 27.01 |57. Seth Devalve: 26.38 |58. Derek Carrier: 25.76 |59. Jake Butt: 25.23 |60. Garrett Celek: 25.09 |
| 61. Jermaine Gresham: 24.76 |62. Orson Charles: 24.67 |63. Jordan Akins: 24.59 |64. Dalton Schultz: 24.57 |65. Joshua Perkins: 23.46 |
| 66. Marcedes Lewis: 22.54 |67. Tyler Conklin: 22.51 |68. Eric Tomlinson: 22.27 |69. Matt Flanagan: 22.02 |70. Ed Dickson: 21.94 |
| 71. Mike Gesicki: 21.46 |72. Ryan Hewitt: 20.98 |73. Levine Toilolo: 20.75 |74. Alex Ellis: 20.6 |75. Donnie Ernsberger: 20.09 |
| 76. Blake Bell: 19.47 |77. Jeremy Sprinkle: 19.01 |78. David Morgan: 18.71 |79. Maxx Williams: 18.6 |80. Hunter Henry: 18.35 |
| 81. Rico Gathers: 17.67 |82. Lance Kendricks: 17.38 |83. Durham Smythe: 16.83 |84. Ross Dwelley: 16.75 |85. Antony Auclair: 15.99 |
| 86. Luke Stocker: 15.6 |87. Scott Simonson: 15.53 |88. Xavier Grimble: 15.35 |89. Ben Braunecker: 15.05 |90. MyCole Pruitt: 14.7 |
| 91. Vance McDonald: 14.47 |92. Dion Sims: 14.35 |93. Deon Yelder: 13.69 |94. Alan Cross: 13.24 |95. John Phillips: 13.18 |
| 96. Brian Parker: 12.49 |97. Sean Culkin: 11.32 |98. Garrett Griffin: 9.38 |99. Lee Smith: 8.85 |100. Gabe Holmes: 8.73 |
| 101. Eric Saubert: 7.87 |102. Darrell Daniels: 7.17 |103. Chris Manhertz: 6.54 |104. Khari Lee: 6.27 |105. Logan Paulsen: 5.59 |
| 106. Johnny Mundt: 4.56 |107. Virgil Green: 3.69 |108. Jerome Cunningham: 3.39 |109. Matt Lengel: 1.6 |110. Clark Harris: 0.68 |
| 111. Hakeem Valles: 0.41 |112. Clive Walford: -1.67 |113. Michael Roberts: -2.24 |114. Tyrone Swoopes: -14.31 | |

## How to train a model:
In main:
* Change "position" variable to train different position models

In FantasyScoreNN:
* Add "and 0" to the line "if(os.path.isfile(self.cLOADBOTPATH))" to allow for retraining of a model
* Alter the model structure or epochs to try to improve results

## Explanation of Visualizations
The players are organized in order of their 2019 ranking.
* Name of player is on the left
* The image in the center is a saliency visualization of the input matrix generated by Keras
    * Years are labeled on the left side, column labels are on the bottom
    * Unlabeled rows/columns are empty (filler) to make each matrix the same size
* The 2018 Prediction, 2018 Actual Scores and 2019 prediction are on the right

All four visualizations can be found in the "Visualizations" folder

## Visualization Examples
<img src="Visualizations/QB-visualization.png" width="99%"/>
<img src="READMEImages/QB-visualization-MattRyan.png" width="99%"/>
