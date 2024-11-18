# Work journal

By Mailin Brandt and Finian Landes

| Date | Duration | Content, Steps, Task | Reflexion |
| :--- | :--- | :--- | :--- |
| 14.10.2024 | 40 min  |  Planing and formulation of “Leitfrage” | We need to modify and add to our “Leitfrage”, as we are not sure how fast we are With our current test train split it might occur that all test images are from one sign |
| 14.10.2024 | 1h | Creating a Test dataset containing 3 times 5 pictures and creating a program to format and rename the pictures | |
| 14.10.2024 | 1h20min | Starting the PCA program creating the Image loading and test train split function - Adding the PCA algorithm from Sheet 6 -> Success rate of 66 or 100% with 3 test items on our 15 item dataset | |
| 21.10.2024 | 1h30min | Created A full Dataset containig 150 Pictures of 10 different Signs, also created a test set with Finians Hand containig 30 Pictures. When running PCA with the original Dataset and taking 30 Test pictures from it the succesrate is over 80% mostly around 90%. When running with Finians hand the success rate is only 50% (This rate is constant as our Train/Test dataset stays constant in this test). |  |
| 21.10.2024 | 1h30min | Added more people to the Dataset but made dataset smaller so only 5 signs. This increased the score when using 2 different instead of 1 to in recognizing an unknown hand to a 93% success rate. With 3 different hands we get a 100% success rate when recognizing an unknown hand. This rate stays constant even when increasing the dataset size to 5 people 4x10 pictures per sign 1x15 pictures per sign| Possibly create another algorithm and compare success rates.|
| 28.10.2024 | 1h30min | Created a function inorder to save images, this did not work for a long time as the image has to be converted to a 8bit integer. Currently this function works only with correct values so 8bit between 0 and 255.  | Upgrade the function so it works with different formats eg 0-1|
| 28.10.2024 | 1h30min  | We started working on the K-means algorithm, currently this does not classify correctly as the centroids often contain NaN values  |  |
| 04.11.2024 | 4h | We continued working on K-means and fixed the NaN error, which was due to empty clusters due to bad initial points. Now we get a new error which lets the Algorithm stop after 2 iterations because the centroids do not continue further | |
| 11.11.2024 | 1h30min | Continued with K-means, algorithm works but the points fed into it ar invalid. | Spend more time careful doing step after step |
| 17.11.2024 | 2h | Refactored and Commented code. Created a Score function for k-means using sklearn as comparison the score there is equal to our k-means implementation -> Implementation is correct | |
| 18.11.2024 | Extended our code to be able to save clusters. And tested some more inputs with their according accuracy. | |
