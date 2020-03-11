# get config
# initialize season
    # c = Crop()
    # c.deserialize(crop)
    # c.build_profit_table(ratio)
    # crop_list.append(c)
# Build routines    
    # find top 5
# Compile routines into schedule
# Build response
# Return it


## VERBS/NOUNS
"""
What do we want to do?

We want to find the optimal routines given a set of values.

-Get/create the values to optimize over.
    - We are optimizing over a set of crops.
    - More specifically we are optimizing over a profit table, by crop.
-Run optimizations
    - an optimization IS a routine. Do routines build themselves? or are they built by something else?
    - Seems like the search for an optimal routine is done external to the routine, then the routine is built.
    - An optimizer should be an object. It takes in data, and finds an optimal routine, given some algorithm.
-Summaries the optimization.
"""
import numpy as np
import pandas as pd

from croptimizer.data.data import seasons, ratios
from croptimizer.utilities import calculate_potential_harvests


class Crop:

    def __init__(self):
        """
        Example usage:
            # Initialize object
            c = Crop()
            c.deserialize(crop_config)
            c.build_profit_table(ratio)

            # Access profit table
            c.profit_table
        """
        pass

    def deserialize(self, crop_config: dict) -> None:
        """
        Constructs Crop object from crop_config json object.

        :param crop_config: Expects a crop_config similar to
        {'amaranth': {'name': 'Amaranth',
                      'url': 'http://stardewvalleywiki.com/Amaranth',
                      'img': 'amaranth.png',
                      'seeds': {'pierre': 70,
                       'joja': 87,
                       'special': 0,
                       'specialLoc': '',
                       'specialUrl': ''},
                      'growth': {'initial': 7, 'regrow': 0},
                      'produce': {'extra': 0,
                       'extraPerc': 0,
                       'rawN': 150,
                       'rawS': 187,
                       'rawG': 225,
                       'jar': 350,
                       'keg': 337,
                       'jarType': 'Pickles',
                       'kegType': 'Juice'}},
        :return: None
        """
        self.name = crop_config['name']
        self.growth = crop_config['growth']
        self.produce = crop_config['produce']
        self.seeds = crop_config['seeds']

    def get_earning_potential(self, ratios: dict, days_remaining_in_month: int) -> float:
        """
        Uses the farming ratios and days remaining in the month to calculate the earning potential
        through the end of the month. Trick: Can be used to also calculate profits in the event
        you wish to abandon a crop, i.e. days_remaining_in_month = 9 is the same profit value
        as starting on day 1 and abandoning crop after 9 days.

        :param ratios: dict, format similar to {'ratioN': 0.97, 'ratioS': 0.02, 'ratioG': 0.01}
        :param days_remaining_in_month: int, must be between 1-28 (inclusive).
        :return: None
        """
        assert days_remaining_in_month > 0
        assert days_remaining_in_month <= 28
        remaining_harvests = calculate_potential_harvests(days_remaining_in_month, self.growth['initial'], self.growth['regrow'])
        profit = 0
        profit += (self.produce['rawN'] 
                 * ratios['ratioN'] 
                 * remaining_harvests)
        profit += self.produce['rawS'] * ratios['ratioS'] * remaining_harvests;
        profit += self.produce['rawG'] * ratios['ratioG'] * remaining_harvests;

        if (self.produce['extra'] > 0):
            profit += self.produce['rawN'] * self.produce['extraPerc'] * self.produce['extra'] * remaining_harvests
        return profit

    def build_profit_table(self, ratios: dict) -> None:
        """
        Iteratively builds a profit table with columns 'days_required' & 'earning_potential' for 
        every day in the month, based on the farming ratios. This table can be accessed as a field
        from the object.

        :param ratios: dict, format similar to {'ratioN': 0.97, 'ratioS': 0.02, 'ratioG': 0.01}
        :return: None
        """
        day_list= np.arange(1, 29)
        profit_table = pd.DataFrame()
        for day in day_list:
            profit_table = profit_table.append({
                'crop':self.name,
                'days_required':day,
                'earning_potential':self.get_earning_potential(ratios, days_remaining_in_month=day)
            }, [0])
        self.profit_table = profit_table.reset_index(drop=True)


class Routine:

    def __init__(self):
        pass


class Schedule:

    def __init__(self):
        self.routines = []


class Scheduler:

    def __init__(self, config: dict):
        self.schedule = Schedule()
        self.config = config
        self.available_crops = self.initialize_season(self.config)

    def initialize_season(self, config: dict) -> list:
        farming_config = config['data']
        climate = farming_config['climate']
        crops = seasons[climate]['crops']
        character_config = farming_config['character']
        farming_ratio = ratios[farming_config['supplement']][character_config['level']]
        available_crops = []
        for crop in crops:
            c = Crop()
            c.deserialize(crop)
            c.build_profit_table(farming_ratio)
            available_crops.append(c)
        return available_crops
