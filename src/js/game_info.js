/**
 * @author S. A. Shenoy
 * @version 0.0.1
 * @date 06/09/2023
 */

// map between schools and their color schemes,
// designed to be consistent across all teams
// from a given school
let TeamCols = new Map ([
    ["auburn",      [0xD23217, 0x585858, 0x1337D3, 0xC4C4C4]],  ["barrington",      [0xE34553, 0x272727, 0xC2C2C2, 0x6AE11E]],  
    ["belmont",     [0xD43D2B, 0x260CC7, 0x1120B3, 0x7A25DA]],  ["belvidere",       [0x9C549C, 0xD7D934, 0x3177CE, 0xC7C7C7]],
    ["canyon",      [0xC61522, 0x363834, 0xC3C234, 0xD98A26]],  ["carbondale",      [0x343434, 0xD4D4D4, 0x2675D9, 0xD926CE]],
    ["c-sandburg",  [0x230DD8, 0xDADA43, 0x4A52B5, 0xBEAD24]],  ["chattahoochee",   [0x320CC7, 0xCBCB54, 0x5A61C3, 0xEAC715]],
    ["choate",      [0xEBEB23, 0x2323A2, 0x4A57C2, 0xA4B4C4]],  ["cincinnati",      [0x8A55AA, 0x113563, 0xEAEAEA, 0xA5B5CA]],
    ["dallas",      [0x7800DB, 0xE9E8E7, 0xABA9AB, 0x162901]],  ["dcc",             [0xEDEDED, 0x2323C3, 0x5E66A1, 0x4245BD]],
    ["dcd",         [0x1212D2, 0xD3D322, 0xEE11BA, 0x1AE530]],  ["elkhorn",         [0x2E2E2E, 0xACACAC, 0xEE2411, 0x1AD2E5]],
    ["fremd",       [0xEAF30D, 0x029715, 0xE01FDE, 0x1A4CE5]],  ["heights",         [0x801010, 0xE3E3E3, 0xCBCB26, 0xB4854B]],
    ["hinsdale",    [0xE0211F, 0xE3E3E3, 0x26CBA0, 0x4B96B4]],  ["hoover",          [0xE0791F, 0x1E1E1E, 0xF1FCFA, 0x59B44B]],
    ["hunter",      [0x931FE0, 0xF1FCFC, 0xEAC3EE, 0x11230E]],  ["innovation",      [0xE0691F, 0xCA4444, 0xF1FCFC, 0x757975]],
    ["irvington",   [0xE7E7E7, 0x1E00DD, 0x6864E2, 0x51519D]],  ["john-adams",      [0xFF2626, 0xF6F6F6, 0x4C47FF, 0xA945A7]],
    ["johns-creek", [0xFF2626, 0xF6F6F6, 0xFFD947, 0xC82525]],  ["kinkaid",         [0xA926FF, 0xF6F6F6, 0xFFD514, 0xA34A5E]],
    ["lincoln-way", [0x2673FF, 0x1D1D1D, 0x14FFC2, 0x30A8BE]],  ["maggie-walker",   [0x14D609, 0xEAEAED, 0xF0EA5B, 0x14B1DA]],
    ["mercer",      [0xF67322, 0x2D2C34, 0xF4F3E9, 0x329FBC]],  ["mexico",          [0xF72C20, 0xEEEDF0, 0xB3B3B3, 0x15B1D9]],
    ["midtown",     [0xBBB5B5, 0xD40000, 0x6885FF, 0x0CE141]],  ["mira-loma",       [0x99CCFF, 0xCC0000, 0xFEFEFE, 0x8D0CE1]],
    ["moberly",     [0xC7161C, 0x2A52BE, 0xFEFEFE, 0xB42BC3]],  ["new-brighton",    [0xB9141A, 0xDDB70B, 0x5AEB00, 0x61DCB2]],
    ["norman",      [0x141414, 0xDDB70B, 0x00EB4D, 0x4E4EEF]],  ["norris",          [0xF0F0F0, 0xDD390B, 0x007BEB, 0x83EF4E]],
    ["northmont",   [0x1BDE2B, 0xF4F22C, 0xCE1DCC, 0x4E6DEF]],  ["parkway-west",    [0x041105, 0xFDFCD7, 0xE00B0B, 0x4EAAEF]],
    ["pl-dunbar",   [0x0A0B0A, 0xF31616, 0x0BE02E, 0x4E75EF]],  ["plymouth",        [0x4055FF, 0xF4F3F3, 0x0BE02E, 0xEF524E]],
    ["r-m",         [0x121214, 0xF7E600, 0xD10BE0, 0x4EBCEF]],  ["saint-joseph",    [0x35DAF7, 0xF0F0EF, 0x221F22, 0xEF5B4E]],
    ["solon",       [0xF1F5F5, 0xF6E724, 0x3F4CBB, 0xD76565]],  ["saint-marks",     [0x3A2EFE, 0xFBEE3D, 0xEFEFF1, 0xDD7CA1]],
    ["stevenson",   [0x0CCC0C, 0xF3E95C, 0xEFEFF1, 0x6AA0EF]],  ["tjhsst",          [0xEDF3ED, 0xFB5954, 0x3528C8, 0x5EF056]],
    ["troy",        [0x111611, 0x949090, 0xDC1414, 0x56F0D0]],  ["uni-lab",         [0xFFA306, 0x3247F2, 0xDC14CE, 0x56F05A]],
    ["usn",         [0xCF0600, 0xA03636, 0xE03DD4, 0xB95C1B]],  ["west-point",      [0x1520DB, 0xF99600, 0x161616, 0xECE30B]],
    ["washington",  [0x1F2BF4, 0xF4F4F2, 0xF91313, 0x1BF551]],  ["walter-payton",   [0x9105ED, 0xFCDE0E, 0xF94513, 0xF51BC3]],
    ["west-point",  [0xE7E6E6, 0x332D05, 0xCF3105, 0x888888]],  ["winnebago",       [0xFDAF18, 0x332D05, 0xBA0DC7, 0x28E997]],
    ["w-churchill", [0x1E2EE1, 0xE1291E, 0x1EE1DE, 0xEDF0EB]],  ["woodlands",       [0x090909, 0xF6B909, 0xC410E4, 0x39FAC3]]
]);

// the names of the two teams playing a game
let team_one = "Barrington";
let team_two = "Auburn";
var team_one_cols = TeamCols[team_one.toLowerCase()];
var team_two_cols = TeamCols[team_two.toLowerCase()];
console.log("team cols " + team_one_cols);

// the names of the players for bot teams
let team_one_players = ["A", "B", "C", "D"];
let team_two_players = ["E", "F", "G", "H"];

/**
 * Function to convert hex to RGB
 * @param col hex color to be converted
 * @returns an array of normalized RGB vals
 */
function hexToRGB(col)
{
    let r = ((col & 0xFF0000) >> 16) / 255.0;
    let g = ((col & 0x00FF00) >> 8)  / 255.0;
    let b = ((col & 0x0000FF))       / 255.0;

    return [r, g, b];
}

function changeCSS(teamOne, teamTwo) {
    var teamOneColors = TeamCols.get(teamOne.toLowerCase());
    var teamTwoColors = TeamCols.get(teamTwo.toLowerCase());
    if (teamOneColors && teamTwoColors) {
        var [primary, secondary, accent, background] = colors;
        document.body.style.setProperty("--primary-color", "#" + primary.toString(16));
        document.body.style.setProperty("--secondary-color", "#" + secondary.toString(16));
        document.body.style.setProperty("--accent-color", "#" + accent.toString(16));
        document.body.style.setProperty("--background-color", "#" + background.toString(16));
    }
}

// code that inserts the shader and uniforms in 
// the html canvas
function loadShaderIntoCanvas(path, team)
{
    let fragment_shader = fs.readFileSync(path).toString();

    var canvas = document.createElement("canvas");
    var sandbox = new GlslCanvas(canvas);
    sandbox.load(fragment_shader);

    let team_col = (team === 0) ? team_one_cols : team_two_cols;

    let col = hexToRGB(team_col);
    sandbox.setUniform("a", col[0], col[1], col[2]);

    col = hexToRGB(team_one_cols[1]);
    sandbox.setUniform("b", col[0], col[1], col[2]);

    col = hexToRGB(team_one_cols[2]);
    sandbox.setUniform("c", col[0], col[1], col[2]);

    col = hexToRGB(team_one_cols[3]);
    sandbox.setUniform("d", col[0], col[1], col[2]); 
}

loadShaderIntoCanvas('../shaders/idle.glsl', 0);
loadShaderIntoCanvas('../shaders/idle.glsl', 1);