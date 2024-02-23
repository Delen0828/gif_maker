/* JAVASCRIPT FOR SLIDER RATINGS - Full 5800 vis */
/* RIGHT NOW: Allows for downloading all images in a given directory */

// set variables
var img;
var pracArray = [];
var imgArray = [];
var i = 0;
var j = 0;
// manually set as per number of images in desired directory
var prac_n = 3;
var n = 5800; // 5800 images
let n_groups = 40;
let items_per_group = 145;

// load images to imgArray
for (i = 0; i < n; i++) {
  img = new Image();
  // push to array (make sure images are named correctly)
  img.src = "resized_stimuli/" + i + ".png";
  imgArray.push("resized_stimuli/" + i + ".png");
}
// load practice images
for (i = 0; i < prac_n; i++) {
  img = new Image();
  // push to array (make sure images are named correctly)
  img.src = "resized_stimuli/" + "practice_" + i + ".png";
  pracArray.push("resized_stimuli/" + "practice_" + i + ".png");
}

// break up imgArray into 40 equal parts
const imgArraySliced = [];
for (let i = 0; i < imgArray.length; i += items_per_group) {
  const chunk = imgArray.slice(i, i + items_per_group);
  imgArraySliced.push(chunk);
}

console.log("sliced Image Array:");
console.log(imgArraySliced);

////////////////////// JSPSYCH //////////////////////

var jsPsych = initJsPsych({
  on_finish: function () {
    // console.log("Thank you for your time taking this survey.")
    // jsPsych.data.displayData('csv');

    // ENTER PROLIFIC REDIRECT:
    // https://app.prolific.com/submissions/complete?cc=CYD6KOJJ
    window.location = "https://app.prolific.com/submissions/complete?cc=CYD6KOJJ";
  },
  preload_images: [
    imgArray,
    pracArray,
    "test_slider_m-2.png",
    "test_slider-2.png",
  ],
});

let cond_arr = [];
for (var i = 1; i <= 40; i++) {
  cond_arr.push(i);
}
cond_arr.map(String);

// create timeline variables — making the dictionary
// CONDITION = cognition-made variable

// uncomment in Cognition:
var i = 0;
var stimuliArray = [];
while (i < cond_arr.length) {
  if (cond_arr[i] == CONDITION) {
    stimuliArray = imgArraySliced[i];
  }

  i++;
}

stimuliArray = jsPsych.randomization.shuffle(stimuliArray);
console.log("check randomization");
console.log(stimuliArray[0], stimuliArray[1], stimuliArray[2]);
pracArray = jsPsych.randomization.shuffle(pracArray);

// add to data
jsPsych.data.addProperties({
  stimuli_order: stimuliArray,
});

var values = [];
for (i = 0; i < stimuliArray.length; i++) {
  temp = {
    image: stimuliArray[i],
  };
  values.push(temp);
}

// Intro page
var enter_fullscreen = {
  type: jsPsychFullscreen,
  message: [
    "Welcome!" +
      "<br>" +
      "<br>" +
      "Your browser must be in full-screen mode for this study. Please click the button below to enter full-screen mode and proceed." +
      "<br>" +
      "<br>",
  ],
  fullscreen_mode: true,
};

// virtual chinrest (credit card) trial
var vc_trial = {
  type: jsPsychVirtualChinrest,
  blindspot_reps: 0,
  resize_units: "cm",
  pixels_per_unit: 50,
};

// virtual chinrest (credit car) pt. 2 — resizing appropriately
var resized_stimulus = {
  type: jsPsychHtmlButtonResponse,
  stimulus: `
    <p>If the measurements were done correctly, the square below should be 10 cm x 10 cm.</p>
    <div style="background-color: black; width: 500px; height: 500px; margin: 20px auto;"></div>
    `,
  choices: ["Continue"],
};

// consent — done in cognition.run

// Attention Check //
// create and randomize options:
var acOptions = [
  "How visually complex it is",
  "How visually simple it is",
  "How attractive it is",
  "How much you like it",
];
acOptions = jsPsych.randomization.shuffle(acOptions);
// create check
var attn_check = {
  type: jsPsychSurveyMultiChoice,
  questions: [
    {
      prompt:
        "ATTENTION CHECK: To demonstrate your understanding, please answer:" +
        "<br>" +
        "<br>" +
        "What criteria are you using to rate a visualization?",
      name: "AttnChk",
      options: acOptions,
      randomize_question_order: true,
      required: true,
    },
  ],
};

// sad ending if participants fail
var sad_ending = {
  type: jsPsychHtmlKeyboardResponse,
  stimulus:
    "You have answered incorrectly. The study is ended." +
    "<br>" +
    "Please close the browser window.",
  choices: "NO_KEYS",
};

// if they passed, they move on to practice trials
var passed_AC = {
  type: jsPsychInstructions,
  pages: [
    "Great! Now you will go through some practice trials." +
      "<br>" +
      "Please use this as a chance to get familiar with the controls.",
  ],
  show_clickable_nav: true,
};

// conditional timeline if they reach the sad ending
var if_failed_AC = {
  timeline: [sad_ending],
  conditional_function: function () {
    var AC_data = jsPsych.data.getLastTrialData().trials[0].response.AttnChk;
    if (AC_data == "How visually complex it is") {
      return false;
    } else {
      return true;
    }
  },
};

// Practice Trials
var prac_trial = {
  type: jsPsychHtmlSliderResponse,
  prompt:
    "<h2>PRACTICE: How visually complex is this chart?</h2>" +
    "<p>You must move the slider before proceeding." +
    "<br>",
  post_trial_gap: 500,
  stimulus: function () {
    return '<img src="' + jsPsych.timelineVariable("pracImage") + '"> ';
  },
  require_movement: true,
  required: true,
  min: 0,
  max: 100,
  start: 50,
  step: 1,
  labels: ["0: Not Complex at all", "25", "50", "75", "100: Extremely Complex"],
  data: {
    pracImage: jsPsych.timelineVariable("pracImage"),
  },
};

var final_instructions = {
  type: jsPsychInstructions,
  pages: [
    "You will now begin the study." + "<br>" + "Select the button to continue.",
  ],
  show_clickable_nav: true,
};

// MAIN TRIAL: add all of the relevant variables to the data field so they
// will appear in the results
var trial = {
  type: jsPsychHtmlSliderResponse,
  prompt:
    "<h2>How visually complex is this chart?</h2>" +
    "<br>" +
    "<p>You must move the slider before proceeding." +
    "<br>",
  post_trial_gap: 500,
  stimulus: function () {
    return '<img src="' + jsPsych.timelineVariable("image") + '">';
  },
  require_movement: true,
  required: true,
  min: 0,
  max: 100,
  start: 50,
  step: 1,
  labels: ["0: Not Complex at all", "25", "50", "75", "100: Extremely Complex"],
  data: {
    image1: jsPsych.timelineVariable("image"),
  },
};

// Demographics
var demographic_intro = {
  type: jsPsychInstructions,
  pages: [
    "Thank you for completing the trials! Next, please fill out the demographic questions on the next page.",
  ],
  show_clickable_nav: true,
};

var demographic_qs = {
  type: jsPsychSurvey,
  pages: [
    [
      {
        type: "text",
        prompt: "What is your age?",
        name: "age",
        placeholder: "Enter a number, e.g. 20",
        required: true,
      },
      {
        type: "multi-choice",
        prompt: "What is your gender?",
        name: "gender",
        options: ["Man", "Woman", "Non-binary", "Other", "Prefer Not to Say"],
        required: true,
      },
      {
        type: "text",
        prompt: "If you selected 'Other', please describe:",
        name: "gender2",
        placeholder: "e.g., Agender",
        required: false,
      },
      {
        type: "multi-choice",
        prompt:
          "What is the highest degree or level of education you have completed?",
        name: "education",
        options: [
          "Some High School",
          "High School",
          "Bachelor's Degree",
          "Master's Degree",
          "Ph.D. or higher",
          "Trade School",
          "None",
        ],
        required: true,
      },
    ],
  ],
};

// PROLIFIC INFO //
// capture info from Prolific
var subject_id = jsPsych.data.getURLVariable("PROLIFIC_PID");
var study_id = jsPsych.data.getURLVariable("STUDY_ID");
var session_id = jsPsych.data.getURLVariable("SESSION_ID");

jsPsych.data.addProperties({
  subject_id: subject_id,
  study_id: study_id,
  session_id: session_id,
});

// Redirect to Prolific // — NOT CURRENTLY USED
var final_trial = {
  type: jsPsychHtmlButtonResponse,
  prompt: `<h2>We appreciate your time and effort.</h2>`,
  choices: ["RETURN TO PROLIFIC"],
  stimulus:
    '<b style="font-size:36px; color:black;">Thank You! Press the button to return to Prolific.</b>' +
    "<br>",
};

// distance check, instructions, attention check
var prelim_trial = {
  timeline: [
    vc_trial,
    resized_stimulus,
    instructions,
    attn_check,
    if_failed_AC,
    passed_AC,
  ],
};

// trials
var main_trial = {
  timeline: [trial], // LEAVE THE BRACKETS IN
  timeline_variables: values,
  randomize_order: true,
};

// demographics
var demographics = {
  timeline: [demographic_intro, demographic_qs],
};

// redirect to prolific —
var redirect_trial = {
  timeline: [final_trial],
};

jsPsych.run([
  enter_fullscreen,
  prelim_trial,
  prac_trial,
  final_instructions,
  main_trial,
  demographics,
  redirect_trial,
]);

////////////////////// FUNCTIONS //////////////////////

/* create function for generating random pairs of images */
function generateRandomPairs(array1, pairsArray) {
  // create an array of all the images, including the duplicates
  const allImages = array1;
  let n = allImages.length;
  let i, j;

  // don't allow an image pair that contains 2 of the same image
  // this code does it! i and j will never be equal
  for (i = 0; i < n; i++) {
    for (j = i + 1; j < n; j++) {
      pairsArray.push([allImages[i], allImages[j]]);
    }
  }

  console.log("There are " + pairsArray.length + " unique combinations.");
}

//// Functions ////

function shuffle(arr) {
  var m = arr.length,
    t,
    i;

  // While there remain elements to shuffle…
  while (m) {
    // Pick a remaining element…
    i = Math.floor(Math.random() * m--);

    // And swap it with the current element.
    t = arr[m];
    arr[m] = arr[i];
    arr[i] = t;
  }

  return arr;
}