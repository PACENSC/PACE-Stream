/**
 * @author S. A. Shenoy
 * @version 0.0.1
 * @date 06/09/2023
 */

let cols:number[] = [0,1,2];

// map between schools and their color schemes,
// designed to be consistent across all teams
// from a given school
let TeamCols = new Map ([
    ["auburn", [0xD23217, 0x585858, 0x1337D3, 0xC4C4C4]], ["barrington",  [0xE34553, 0x272727, 0xC2C2C2, 0x6AE11E]],  
    ["belmont", [0]], ["belvidere", [0]],
    ["canyon_crest", [0]], ["carbondale", [0]],
    ["carl_sandburg", [0]], ["chattahoochee", [0]],
    ["choate", [0]], ["cincinnati", [0]],
    ["dallas", [0]], ["dcc", [0]],
    ["dcd", [0]], ["elkhorn_north", [0]],
    ["fremd", [0]], ["heights", [0]],
    ["hinsdale_central", [0]], ["hoover", [0]],
    ["hunter", [0]], ["innovation", [0]],
    ["irvington", [0]], ["john_adams", [0]],
    ["johns_creek", [0]], ["kinkaid", [0]],
    ["lincoln-way", [0]], ["maggie_walker", [0]],
    ["mercer", [0]], ["mexico", [0]],
    ["midtown", [0]], ["mira_loma", [0]],
    ["moberly", [0]], ["new_brighton", [0]],
    ["norman", [0]], ["norris", [0]],
    ["northmont", [0]], ["parkway_west", [0]],
    ["pl_dunbar", [0]], ["plymouth", [0]],
    ["rm", [0]], ["saint_joseph", [0]],
    ["solon", [0]], ["st_marks", [0]],
    ["stevenson", [0]], ["tj", [0]],
    ["troy", [0]], ["uni_lab", [0]],
    ["usn", [0]], ["walter_payton", [0]],
    ["washington", [0]], ["waukee", [0]],
    ["west_point", [0]], ["winnebago", [0]],
    ["w_churchill", [0]], ["woodland", [0]]
]);

// the names of the two teams playing a game
let team_one = "Barrington";
let team_two = "Auburn";

/**
 * Function to convert hex to RGB
 * @param col hex color to be converted
 * @returns an array of normalized RGB vals
 */
function hexToRGB(col : number)
{
    let r = ((col & 0xFF0000) >> 16) / 255.0;
    let g = ((col & 0x00FF00) >> 8)  / 255.0;
    let b = ((col & 0x0000FF))       / 255.0;

    return [r, g, b];
}

function linkUniforms()
{

}

/**
    // Auburn High School A (Rockford, IL) – Fully Paid
    // Barrington A (Barrington, IL) – Fully Paid
    // Belmont (Belmont, MA) – Fully Paid
    // Belvidere High School (Belvidere, IL) – Fully Paid
    // Canyon Crest (San Diego, CA)
    // Carbondale High School (Carbondale, IL) – Fully Paid
    // Carl Sandburg High School A (Plainfield, IL) – Fully Paid
    // Chattahoochee A (Johns Creek, GA) – Fully Paid
    // Choate A (Wallingford, CT) – Fully Paid
    // Cincinnati Hills Christian Academy A (Cincinnati, OH) – Fully Paid
    // Dallas County Academic Team (Fair Grove, MO) – Fully Paid
    // Detroit Catholic Central A (Novi, MI) – Fully Paid
    // Detroit Country Day School (Beverly Hills, MI) – Fully Paid
    // Elkhorn North High School (Omaha, NE) – Fully Paid
    // Fremd A (Palatine, IL) – Fully Paid
    // Heights High School (Houston, TX) – Fully Paid
    // Hinsdale Central (Hinsdale, IL) – Fully Paid
    // Hoover High School A (Hoover, AL) – Fully Paid
    // Hunter College High School A (New York, NY) – Fully Paid
    // Innovation Academy A (Alpharetta, GA) – Fully Paid
    Irvington High School A (Fremont, CA) – Fully Paid
    John Adams High School A (South Bend, IN) – Fully Paid
    Johns Creek A (Johns Creek, GA) – Fully Paid
    Kinkaid (Houston, TX) – Fully Paid
    Lincoln-Way East High School (Frankfort, IL) – Fully Paid
    Maggie Walker A (Richmond, VA) – Fully Paid
    Mercer County Academic Team (Princeton, NJ 08540) – Fully Paid
    Mexico High School A (Mexico, MO) – Fully Paid
    Midtown High School (Atlanta, GA) – Fully Paid
    Mira Loma High School (Sacramento, CA) – Fully Paid
    Moberly High School (Moberly, MO) – Fully Paid
    New Brighton Academic Team (New Brighton, MN) – Fully Paid
    Norman High School (Norman, OK) – Fully Paid
    Norris A (Firth, NE) – Fully Paid
    Northmont High School A (Clayton, OH) – Fully Paid
    Parkway West High School (Ballwin, MO) – Fully Paid
    Paul Laurence Dunbar (Lexington, KY) – Fully Paid
    Plymouth Academic Team (Plymouth, MN) – Fully Paid
    Richard Montgomery High School A (Rockville, MD 20852) – Fully Paid
    Saint Joseph (South Bend, IN) – Fully Paid
    Solon High School (Solon, OH) – Fully Paid
    St. Mark’s School of Texas (Dallas, TX) – Fully Paid
    Stevenson A (Lincolnshire, IL) – Fully Paid
    Thomas Jefferson Science & Tech A (Alexandria, VA 22312) – Fully Paid
    Troy A (Troy, MI) – Fully Paid
    Uni Lab A (Urbana, IL) – Fully Paid
    University School of Nashville A (Nashville, TN) – Fully Paid
    Walter Payton College Prep A (Chicago, IL) – Fully Paid
    Washington High School A (Washington, MO) – Fully Paid
    Waukee High School (Waukee, IA) – Fully Paid
    West Point High School (Cullman, AL 35057) – Fully Paid
    Winnebago High School (Winnebago, IL) – Fully Paid
    Winston Churchill A (Potomac, MD) – Fully Paid
    Woodland Regional High School (Beacon Falls, CT) – Fully Paid
*/