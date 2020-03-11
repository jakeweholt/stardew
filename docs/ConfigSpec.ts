// Tyeps related to my config files 
type Climate = "Spring" | "Summer" | "Fall" | "Greenhouse";


export type Fertilizer = "Basic" | "Quality";
export type SpeedGro = "Regular" | "Deluxe";

// A square can have a maximum of one supplement
// (there are other supps, but they don't apply)
type Supplement = undefined | Fertilizer | SpeedGro;

// The orginal data just considers "special", which is
// too broad a category to be useful. This breaks it up.
type VendorList = {
  pierre: boolean,
  jojamart: boolean,
  oasis: boolean,
  cart: boolean,
  events: boolean
}

type Character = {
  level: number,
  hasTiller: boolean,
  levelTenPerk: undefined | "Agriculturalist" | "Artisan";
}

class StardewConfig {
  climate:Climate;
  supplement:Supplement;
  days:number;
  // In seasonal climates, "days" input is the number
  // remaining in the month. In "Greenhouse" mode,
  // it's the number of days to use for the projection,
  // because the growing period is unlimited.
  projectionLength:number = (this.climate == 'Greenhouse') ? days : (28 - days);
  
  // Some crops can grow across two seasons, a few can grow across 3.
  // If we're checking for the best result in spring, we may have to also
  // model a hypothetical summer to see whether it's worth holding a
  // multi-season crop across that period as well.
  multiSeason: boolean;

  // these 3 processing modes are independent. All 3 can be on,
  // and the same crop will have a separate entry for each.
  useRaw: boolean;
  useJar: boolean;
  useKeg: boolean;

  // API can return total and I can do the averaging client side,
  // or however else you want to do it.
  displayProfit: 'dayAvg' | 'totalProfit' | 'both';

  // When false, seed costs are withdrawn from profit
  freeSeeds: boolean;

  // See note on type
  vendors: VendorList;
}