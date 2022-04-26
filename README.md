# NFL_salarycap_optimization


# Table of Contents

1) [Business Understanding](#business_understanding)  
2) [Data Background and Limitations](#data_and_limitations)  
3) [EDA and Data Cleaning](#EDA_data_cleaning)  
4) [Modeling](#modeling)  
&nbsp;&nbsp;&nbsp;&nbsp;4a. [Baseline](#Baseline)  
&nbsp;&nbsp;&nbsp;&nbsp;4b. [Logistic Regression](#log_reg)  
&nbsp;&nbsp;&nbsp;&nbsp;4c. [Decision Tree](#dtree)  
&nbsp;&nbsp;&nbsp;&nbsp;4d. [Optimization](#func)  
5) [Feature Engineering](#feat)  
6) [Conclusions](#conc)  
&nbsp;&nbsp;&nbsp;&nbsp;6a. [Future Research](#future)  

---

# 1) Business Understanding <a class="anchor" id="business_understanding"></a>

**Hypothetical Business Background**: In an effort to broaden its audience, the NFL is expanding its roster from 32 teams to 34 teams with two new franchises to be located in London, UK and Vancouver, CA. We have been approached by the ownership group from one of the cities and they are eager to establish themselves as serious contenders to maximize public interest and in turn, revenue.

**Problem**: The ownership group has asked us how their team can best maximize win percentage during the regular season (17 games)  by looking at how to best allocate their available "Salary Cap" (league-imposed spending limit on players).

**Goals**: Scrape historic NFL data to predict a team's regular season win percentage given how much they spend on different player position groups and provide recommendations on how they should best spend their salary cap.

---

# 2) Data Background and Limitations <a class="anchor" id="Data Background and Limitations"></a>

###  **Data Background**
   - Data scraped from <a href="https://www.spotrac.com/">spottrac.com</a>
       - Link to notebook [Scraping/Cleaning Notebook](./relative/path/to/notebook)
   - Dataset contains details about every player contract, how it affects the Salary Cap and the player's position
   - This includes players that are no longer on the team, provided their contracts still affect the Salary Cap that year  


###  **Data Limitations**
   - A paywall only lets us access 3 years (2019 - 2021)
   - Data does not factor in player performance

---

# 3) EDA and Data Cleaning <a class="anchor" id="EDA_data_cleaning"></a>
### Format:
   - **General Description** 
      - Reasoning


   - **Combine 96 scrapes from separate web pages into 3 year based lists** 
       - Data from scrapes did not contain year or team info
   - **Add standard team abbreviations and years as new columns to dataframes**
       - Required for sorting
   - **Rename first column to "Status" and overwrites column values with player status from dataframe**
       - Protects player identity and any possible bias associated with names
       - Player status is useful data while the names were arbitrary
       - Cleans up the column name for merging
   - **Filtered dataframe and clean cells**
       - Only want relevant data that is usable
   - **Pulled in regular season win % from separate dataframe**
       - Need to pull in target data
   - **Bin player positions into groups based on player roles**
       - Many player positions are similar and 23 is too many
   - **Bin regular season win% into high, average and low based on percentiles**
       - For modeling purposes
   - **Add column for total Salary Cap per team/year**
       - Changes from year to year based on limits and team usage
   - **Group data by position group/year and bin spending based on percentiles**
       - For feature engineering       
       

Notebook with granular details [Scraping/Cleaning Notebook](https://github.com/chris161011/NFL_salarycap_optimization/blob/main/data/scraping_notebook.ipynb)

---

## &nbsp;&nbsp;&nbsp;&nbsp; 4a. Baseline Model <a class="anchor" id="Baseline"></a>

![alt text](https://github.com/chris161011/NFL_salarycap_optimization/blob/main/Images/Dummy.PNG)

---  
## &nbsp;&nbsp;&nbsp;&nbsp; 4b. Logistic Regression <a class="anchor" id="log_reg"></a>  

![alt text](https://github.com/chris161011/NFL_salarycap_optimization/blob/main/Images/Log_reg.PNG)

## &nbsp;&nbsp;&nbsp;&nbsp; 4c. Decision Tree <a class="anchor" id="dtree"></a>  

![alt text](https://github.com/chris161011/NFL_salarycap_optimization/blob/main/Images/Dec_T.PNG)

---  
## &nbsp;&nbsp;&nbsp;&nbsp; 4d. Optimization <a class="anchor" id="func"></a>  

&nbsp;&nbsp;&nbsp;&nbsp; We achieved close enough scores with both Logistic Regression and Decision Trees that I believe it warrants optimizing both.  

![alt text](https://github.com/chris161011/NFL_salarycap_optimization/blob/main/Images/Log_reg_opt.PNG)

The optimized Decision Tree scored a whopping 96.1% accuracy! This will be our final model.  

![alt text](https://github.com/chris161011/NFL_salarycap_optimization/blob/main/Images/fnl_mod.PNG)

---  
# 5) Feature Engineering <a class="anchor" id="feat"></a>  

![alt text](https://github.com/chris161011/NFL_salarycap_optimization/blob/main/Images/corr_table.PNG)

---  
# 6) Conclusions <a class="anchor" id="conc"></a>  

When provided with the amount spent on each position group, player status and age, we can predict whether or not that team will have a high win percentage (75th percentile or above) with 96% accuracy!  

Since that information is relatively easy to come by and control, our model should be immensely helpful in resolving our stakeholders business problem of maximizing win percentage.  

Other conclusions we can draw from our research include the top three most positively correlated position group to regular season win percentage which are..  

- spending an average amount on receivers (.241)
- spending a high amount on defensive line (.177)
- spending an average amount on kickers (.153)  

And the top three most negatively correlated position group to regular season win percentage which are...  

- spending a low amount on kickers (-.188)
- spending a low amount on receivers (-.177)
- spending a low amount on linebackers (-.122)  

---  
# &nbsp;&nbsp;&nbsp;&nbsp; 6a. Future Research <a class="anchor" id="future"></a>  

#### &nbsp;&nbsp;&nbsp;&nbsp; Some Future research our stakeholders will want to consider includes...  

- Since this is a fresh team and we have the rare opportunity of only signing active players for our first year, it would behoove us to look at models optimized only for 'active' player status for the first year.
- It would also be worth paying for access to more years worth of data to make our dataset more robust.
    - Although I would caution going to far back, as the game and its strategies evolve over time
- Our next model should focus on player performance so we can maximize our spending in each category
- Given the jack-of-all trades nature of some modern positions like TE or Runningback, we should look at individual team usage of positions and allocate their salary accordingly to their usage.  
