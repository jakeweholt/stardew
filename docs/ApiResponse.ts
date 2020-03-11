type ApiResponse = {
  // A copy of the options JSON that led to these results
  options: StardewConfig,
  // results are an array of Schedules, ordered by profitability
  results: Schedule[]
}

// A schedule is a sequence of crops whose harvests fit
// within the specified period, but the post-harvest
// parts of a routine can extend beyond the period.

type Schedule = {
  // open to other things here, eg array of profit per day, whatever
  totalProfit: number,
  // An array of routines in chronological order.
  // Routines can overlap as long as two crops are
  // never alive at the same time.
  // A routine can extend beyond the day of the month
  routines: Routine[]
}

// A routine is a series of events describing
// the entire lifecycle of one crop on one tile.

// Purchased once
// Planted once
// Harvested 0 or more times
// Processed in one of 3 ways
// Sold after processing

type Routine = {
  // -------------------------------
  // PLANTING
  // -------------------------------

  purchasePrice: number,

  // Dates are relatve to the start of the schedule.
  // crop growth ticks when night falls on a watered tile,
  // so seed growth time is best thought of in terms of 
  // watered nights. Plant day counts as day 0, not 1.
  plantDate: number,

  // this is the smallest of
  // * harvest time for one-off crops
  // * days until a season that will kill the plant
  // * the growing period given if in Greenhouse mode
  daysAlive: number,

  // -------------------------------
  // HARVEST
  // -------------------------------

  // A harvest is the capturing of resources from a crop.
  // Lifespan before or after the harvest is not a factor.
  // Profit from later processing or sale is not a factor.

  // array of harvest times, expressed as watered nights
  // since plantDate
  harvestDates: number[],

  // Effective drop rate for one tile,
  // rounded to two decimal places
  itemsPerHarvest: number,
  
  // -------------------------------
  // PROCESSING
  // -------------------------------

  // an item can only be  processed one way
  processType: "raw" | "keg" | "jar",

  // -------------------------------
  // Sale
  // -------------------------------

  // assuming that crops are processeed upon harvest,
  // this is relativeHarvestDates => date + processType.duration 
  // the last of these dates marks the duration of the routine.
  saleDates: number[],

  // The total profit for one tile with this routine
  profit: number
}