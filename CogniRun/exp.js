var jsPsych = initJsPsych();
var timeline = [];
const TRIALNUM=10
jsPsych.pluginAPI.preloadImages(
  ["1.png","2.png","3.png","4.png","mean_sample.png","variance_sample.png","spike_sample.png","mean_test.png","variance_test.png","spike_test.png","seq_trace_his.gif","seq_notrace_his.gif","seq_notrace_nohis.gif","seq_trace_nohis.gif","sync_trace.gif","sync_notrace.gif","static.png"],
  function(){startExperiment();})

var operationIntro = {
  type: jsPsychHtmlButtonResponse,
  stimulus: "<p>Due to compatibility issues, please <b>DO NOT USE SAFARI</b>.</p> <p>In this survey you will follow some instructions, read animated visualizations, <br> and answer questions based on the visualization you read.</p> <p> This study is built on a computer setting, so please make sure you are using a computer setup <br>(e.g. laptop, computer with a moniter and keyboard).</p>",
  choices: ["Continue"]
}  
timeline.push(operationIntro)

// Intro page
var enter_fullscreen = {
  type: jsPsychFullscreen,
  message: [
      "<br>" +
      "<br>" +
      "Your browser must be in full-screen mode for this study. <br> Please click the button below to enter full-screen mode and proceed." +
      "<br>" +
      "<br>",
  ],
  fullscreen_mode: true,
};
timeline.push(enter_fullscreen)
// virtual chinrest (credit card) trial
var vc_trial = {
  type: jsPsychVirtualChinrest,
  blindspot_reps: 0,
  resize_units: "cm",
  pixels_per_unit: 50,
};
timeline.push(vc_trial)

// virtual chinrest (credit car) pt. 2 — resizing appropriately
var resized_stimulus = {
  type: jsPsychHtmlButtonResponse,
  stimulus: `
    <p>If the measurements were done correctly, the square below should be 10 cm x 10 cm.</p>
    <div style="background-color: black; width: 500px; height: 500px; margin: 20px auto;"></div>
    `,
  choices: ["Continue"],
};
timeline.push(resized_stimulus)

var prolificID = {
  type: jsPsychSurveyText,
  questions:
  [
  {prompt: "Please enter your Prolific ID in the text below. <br>Double check since you will get compensated based on the ID you provide.",required: true}
  ],
  
}  
timeline.push(prolificID)

var chartReadIntro = {
  type: jsPsychHtmlButtonResponse,
  stimulus: 'You will now see 4 questions that each asks you to read a chart and answer a question related to the given chart.',
  choices: ["Continue"]
}
timeline.push(chartReadIntro)

var chartRead1 = {
  type: jsPsychImageButtonResponse,
  stimulus: '2.png',
  choices: ['60-70km', '30-40km', '20-30km', '50-60km'],
  prompt: "What distance have customers traveled in the taxi the most?"
}
timeline.push(chartRead1)

var chartRead2 = {
  type: jsPsychImageButtonResponse,
  stimulus: '3.png',
  choices: ['Beijing','Shanghai','London','Seoul'],
  prompt: "Which city’s metro system has the largest number of stations?"
}
timeline.push(chartRead2)

var chartRead3 = {
  type: jsPsychImageButtonResponse,
  stimulus: '4.png',
  choices: ['$50.54','$47.02','$42.34','$43.48'],
  prompt: "What was the price of a barrel of oil in February 2020?"
}
timeline.push(chartRead3)

var chartRead4 = {
  type: jsPsychImageButtonResponse,
  stimulus: '1.png',
  choices: ['$0.71','$0.90','$0.80','$0.63'],
  prompt: "What was the average price of a pound of coffee in October 2019?"
}
timeline.push(chartRead4)

var instructIntro = {
  type: jsPsychHtmlButtonResponse,
  stimulus: 'Next, we will look at two concepts that data analysts care a lot about when reading visualizations: mean and variance.',
  choices: ["Continue"]
}
timeline.push(instructIntro)

var meanDef = {
  type: jsPsychImageButtonResponse,
  stimulus_height: 525,
	stimulus_width: 809,
  stimulus: 'mean_sample.png',
  choices: ["Continue"],
  prompt: "<p>You see two sets of lines in the following visualizations, <b style='color:red'>red</b> and <b>black</b>. </p> <p>The <b>mean</b> value of the solid <b style='color:red'>red</b> line in this chart is measured by its overall position on the chart, as indicated by the <b style='color:red'>red</b> dashed line, which is approximately 4. The mean value of the solid <b>black</b> line is indicated by the black dashed line, which is approximately -4. </p> <p>With the vertical y-axis ranging from -20 to +20, we see that the higher the overall position of the line, the higher mean value it has.</p>",
  // trial_duration: 5000  
};
timeline.push(meanDef)

// trail_correct=false

var meanDefQ = {
  type: jsPsychImageButtonResponse,
  stimulus: 'mean_sample.png',
  stimulus_height: 525,
	stimulus_width: 809,
  choices: ['Black','Red','I have no idea'],
  prompt: "Which line has the highest mean value?",
  on_finish: function(data){
    if(data.response == 1){
      data.correct = true;
    } else {
      data.correct = false; 
    }
  }
}

//TODO: I have no idea (remove Incorrect)

var feedback = {
  type: jsPsychHtmlButtonResponse,
  choices: ['Continue'],
  stimulus: function(){
    var last_trial_correct = jsPsych.data.get().last(1).values()[0].correct;
    if(last_trial_correct){
      return "<p>Correct!</p>"; // the parameter value has to be returned from the function
    } else {
      return "<p>Incorrect. The red line has a higher overall position, thus it has a higher mean.</p>"; // the parameter value has to be returned from the function
    }
  }
}

var loop_node = {
    timeline: [meanDefQ,feedback],
    loop_function: function(data){return (!jsPsych.data.get().last(2).values()[0].correct);}
}

timeline.push(loop_node);



var varDef = {
  type: jsPsychImageButtonResponse,
  stimulus_height: 525,
	stimulus_width: 809,
  stimulus: 'variance_sample.png',
  choices: ["Continue"],
  prompt: "<p><b>Variance</b> is a measure of <b>how far</b> and <b>how frequently</b> the data is spread out from the mean. The farther and more frequently the data moves away from the mean, the higher the variance. </p> <p> In the chart below, the <b style='color:red'>red</b> area highlights the amount the <b style='color:red'>red</b> line spreads out from the mean. The <b>grey</b> area highlights the amount the <b>black</b> line spreads out from the mean. </p> <p> Approximately, the larger the area highlighted, the higher the variance.</p>",
  // trial_duration: 5000  
};
timeline.push(varDef)

var varDefQ = {
  type: jsPsychImageButtonResponse,
  stimulus: 'variance_sample.png',
  stimulus_height: 525,
	stimulus_width: 809,
  choices: ['Black','Red','I have no idea'],
  on_finish: function(data){
    if(data.response == 1){
      data.correct = true;
    } else {
      data.correct = false; 
    }
  },
  prompt: "Which line has the highest variance?"
};

var feedback = {
  type: jsPsychHtmlButtonResponse,
  choices: ['Continue'],
  stimulus: function(){
    var last_trial_correct = jsPsych.data.get().last(1).values()[0].correct;
    if(last_trial_correct){
      return "<p>Correct!</p>"; // the parameter value has to be returned from the function
    } else {
      return "<p>Incorrect. The red line moves farther and more frequently away from the mean, thus the red line has a higher variance.</p>"; // the parameter value has to be returned from the function
    }
  }
}

var loop_node = {
    timeline: [varDefQ,feedback],
    loop_function: function(data){return (!jsPsych.data.get().last(2).values()[0].correct);}
}

timeline.push(loop_node);

var meanTest = {
  type: jsPsychHtmlButtonResponse,
  stimulus: "<p>To test your understanding of mean and variance, try to answer the following two questions.</p>",
  choices: ["Continue"]
};
timeline.push(meanTest)

var meanTestQ = {
  type: jsPsychImageButtonResponse,
  stimulus: 'mean_sample.png',
  stimulus_height: 525,
	stimulus_width: 809,
  choices: ['Black','Red','I have no idea'],
  prompt: "Which line has the highest mean value?",
  on_finish: function(data){
    if(data.response == 1){
      data.correct = true;
    } else {
      data.correct = false; 
    }
  }
}

var feedback = {
  type: jsPsychHtmlButtonResponse,
  choices: ['Continue'],
  stimulus: function(){
    var last_trial_correct = jsPsych.data.get().last(1).values()[0].correct;
    if(last_trial_correct){
      return "<p>Correct!</p>"; // the parameter value has to be returned from the function
    } else {
      return "<p>Incorrect. The red line has a higher overall position, thus it has a higher mean.</p>"; // the parameter value has to be returned from the function
    }
  }
}

var loop_node = {
    timeline: [meanTestQ,feedback],
    loop_function: function(data){return (!jsPsych.data.get().last(2).values()[0].correct);}
}

timeline.push(loop_node);

var varTestQ = {
  type: jsPsychImageButtonResponse,
  stimulus: 'variance_test.png',
  stimulus_height: 525,
	stimulus_width: 809,
  choices: ['Black','Red','I have no idea'],
  on_finish: function(data){
    if(data.response == 0){
      data.correct = true;
    } else {
      data.correct = false; 
    }
  },
  prompt: "Which line has the highest variance?"
};

var feedback = {
  type: jsPsychHtmlButtonResponse,
  choices: ['Continue'],
  stimulus: function(){
    var last_trial_correct = jsPsych.data.get().last(1).values()[0].correct;
    if(last_trial_correct){
      return "<p>Correct!</p>"; // the parameter value has to be returned from the function
    } else {
      return "<p>Incorrect. The black line moves farther and more frequently away from the mean, thus the red line has a higher variance.</p>"; // the parameter value has to be returned from the function
    }
  }
}

var loop_node = {
    timeline: [varTestQ,feedback],
    loop_function: function(data){return (!jsPsych.data.get().last(2).values()[0].correct);}
}

timeline.push(loop_node);


var spikeDef = {
  type: jsPsychImageButtonResponse,
  stimulus: 'spike_sample.png',
  choices: ["Continue"],
  prompt: "<p>We also introduce the concept of a <b>significant spike</b>. We refer to a line as having the more significant spike if it contains the highest spike among all the spikes. The height of the spike is determined based on the difference between the peak of the spike and the mean value of the line containing the spike.</p>",
  // trial_duration: 5000  
};
timeline.push(spikeDef)

var spikeDef2 = {
  type: jsPsychImageButtonResponse,
  stimulus: 'spike_sample.png',
  // stimulus_height: 525,
  choices: ["Continue"],
  prompt: "<p>To determine whether a line contains the most significant spike, we first identify the highest spike for each line. <br>For the <b>black</b> line, it would be the first spike near the x-value of -7.5. <br>For the <b style='color:red'>red</b> line, it would be the last spike near the x-value of +7.5.<br>Next, we compare these two spikes to see which one is bigger compared to the mean value of the line. <br>For the <b>black</b> line, which has a mean value of around 5, the spike goes up to 18, which is an increase of 18 - 5 = 13 units. <br>For the <b style='color:red'>red</b> line, which has a mean value of around -5, the spike goes up to around 3, which is an increase of 3 - (-5) = 8 units. <br>Because 13 units is greater than 8 units, we conclude that the <b>black</b> line has the more significant spike.</p>",
  // trial_duration: 5000  
};
timeline.push(spikeDef2)

var spikeDefQ = {
  type: jsPsychImageButtonResponse,
  stimulus: 'spike_sample.png',
  // stimulus_height: 525,
  choices: ['Black','Red','I have no idea'],
  on_finish: function(data){
    if(data.response == 0){
      data.correct = true;
    } else {
      data.correct = false; 
    }
  },
  prompt: "Which line has the most significant spike?"
};

var feedback = {
  type: jsPsychHtmlButtonResponse,
  choices: ['Continue'],
  stimulus: function(){
    var last_trial_correct = jsPsych.data.get().last(1).values()[0].correct;
    if(last_trial_correct){
      return "<p>Correct!</p>"; // the parameter value has to be returned from the function
    } else {
      return "<p>Incorrect. The biggest spike in the black line is taller than the biggest spike in the red line, hence the black line has the most significant spike. </p>"; // the parameter value has to be returned from the function
    }
  }
}

var loop_node = {
    timeline: [spikeDefQ,feedback],
    loop_function: function(data){return (!jsPsych.data.get().last(2).values()[0].correct);}
}

timeline.push(loop_node);

var spikeTest = {
  type: jsPsychHtmlButtonResponse,
  stimulus: "<p>To test your understanding of significant spike, try to answer the following question.</p>",
  choices: ["Continue"]
};
timeline.push(spikeTest)

var spikeTestQ = {
  type: jsPsychImageButtonResponse,
  stimulus: 'spike_test.png',
  // stimulus_height: 525,
  choices: ['Black','Red','I have no idea'],
  on_finish: function(data){
    if(data.response == 0){
      data.correct = true;
    } else {
      data.correct = false; 
    }
  },
  prompt: "Which line has the most significant spike?"
};

var feedback = {
  type: jsPsychHtmlButtonResponse,
  choices: ['Continue'],
  stimulus: function(){
    var last_trial_correct = jsPsych.data.get().last(1).values()[0].correct;
    if(last_trial_correct){
      return "<p>Correct!</p>"; // the parameter value has to be returned from the function
    } else {
      return "<p>Incorrect. The biggest spike in the black line is taller than the biggest spike in the red line, hence the black line has the most significant spike. </p>"; // the parameter value has to be returned from the function
    }
  }
}

var loop_node = {
    timeline: [spikeDefQ,feedback],
    loop_function: function(data){return (!jsPsych.data.get().last(2).values()[0].correct);}
}

timeline.push(loop_node);

///------Real Experiment------///

for (var rp=0;rp<TRIALNUM;rp++){
var pickID=jsPsych.randomization.randomInt(0,filelist.length)
var gif_name=filelist[pickID]
// console.log(gif_name)
var trial_FLAG=true
var ctrl_FLAG=false
var gif_prompt="<p>Study this vis for 5 seconds.</p>"
if (rp===0){
  gif_name="seq_trace_his_4_AVGhhhh_VARhhhh_SPIKEhhhh_bypg_4.mp4";
  trial_FLAG=false;
  ctrl_FLAG=true;
  gif_prompt="This is an animated visualization.<br>You can study it for any time you like.<br>Press <b>Continue</b> when you are ready to answer questions."
  var warmUpMsg = {
    type: jsPsychHtmlButtonResponse,
    stimulus: `In the following part, you will see ${TRIALNUM+1} animated visualizations for 5 seconds and answer three questions about each visualization. <br> The first one will be a warm-up trail without time limit and will not be recorded.`,
    choices: ["Continue"]
  }
  timeline.push(warmUpMsg)
}
if (rp===1){
    var warmUpMsg2 = {
    type: jsPsychHtmlButtonResponse,
    stimulus: `Great Job! Next you will see the rest ${TRIALNUM} animated visualizations.<br>You only have 3 to 5 seconds this time, and no pause or replay are allowed.`,
    choices: ["Continue"]
  }
  timeline.push(warmUpMsg2)
}

var gifShow = {
    type: jsPsychVideoButtonResponse,
    stimulus: [gif_name],
    choices: ["Continue"],
    prompt: gif_prompt,
    trial_ends_after_video: trial_FLAG,
    response_allowed_while_playing: false,
    controls: ctrl_FLAG
};
timeline.push(gifShow);

///---Option---///
const regex = /_([^_]+)\_[0-9].mp4/;
// const regex = /_([^_]+).mp4/;
const match = regex.exec(gif_name)[1];
// console.log(match)
var line_num=match.length
var Option = [];
for (var i=0;i<line_num;i++){
	var color=''
	switch(match[i]){
		case 'g' : color="<font style='color: #117733;'>Green</font>"; break;
		case 'b' : color="<font style='color: #88CCEE;'>Blue</font>"; break;
		case 'y' : color="<font style='color: #DDCC77;'>Yellow</font>"; break;
		case 'p' : color="<font style='color: #AA4499;'>Purple</font>"; break;
		default: color='NOT_DEFINED'; break;
	}
	Option.push(color);
}

Option = jsPsych.randomization.shuffle(Option);
var avgCheck = {
  type: jsPsychSurveyMultiChoice,
  questions: [
    {
      prompt:
        "Which line has highest mean value?",
      options: Option,
      // preamble: "hello",
      randomize_question_order: true,
      required: true,
    },
  ],
};
timeline.push(avgCheck);

var varCheck = {
  type: jsPsychSurveyMultiChoice,
  questions: [
    {
      prompt:
        "Which line has highest variance?",
      options: Option,
      randomize_question_order: true,
      required: true,
    },
  ],
};

timeline.push(varCheck)

var spikeCheck = {
  type: jsPsychSurveyMultiChoice,
  questions: [
    {
      prompt:
        "Which line has the most significant spike?",
      options: Option,
      randomize_question_order: true,
      required: true,
    },
  ],
};

timeline.push(spikeCheck);
}

var sortIntro = {
  type: jsPsychHtmlButtonResponse,
  stimulus: "<p> Great job! In the next question you will be asked to rank different types of animated visualizations.</p>",
  choices: ["Continue"]
}  
timeline.push(sortIntro)

var sort_trial = {
    type: jsPsychFreeSort,
    stimuli: ["seq_trace_his.gif","seq_notrace_his.gif","seq_notrace_nohis.gif","seq_trace_nohis.gif","sync_trace.gif","sync_notrace.gif","static.png"],
    stim_width: 160,
    stim_height: 120,
    sort_area_width: 1400,
    sort_area_height: 180,
    sort_area_shape: "square",
    stim_starts_inside: true,
    counter_text_finished: ' ',
    prompt: "<div><p>Click and drag the visualizations below to sort them so that they are ranked from the left to the right based on your preference.</p><p><b>LEFT</b> represents <b>DISLIKE</b> while <b>RIGHT</b> represents <b>LIKE</b>.</p></div> <div id='label-dislike' style='position: absolute; left: 10%; top: 35%; transform: translateY(-50%); font-weight: bold; font-size:24px'>DISLIKE</div> <div id='label-like' style='position: absolute; right: 10%; top: 35%; transform: translateY(-50%); font-weight: bold; font-size:24px'>LIKE</div> <div id='label-neutral' style='position: absolute; left: 50%; top: 35%; transform: translateY(-50%); font-weight: bold; font-size:24px'>NEUTRAL</div>"
};  
timeline.push(sort_trial)

/// -------- Demographics -------- ///
var demoQ={
    type: jsPsychSurvey,
    css_classes: ['survey'],
    pages: [[
      {
        type: 'multi-choice',
        prompt: "Which of the following best describes your gender?", 
        name: 'Gender', 
        options: ['Female','Male','Non-binary','Prefer not to say',"I'd like to describe myself"], 
        required: true,
        required_error: "Please answer the question.",
        required_question_label: "*"
      }, 
     {
        type: 'text',
        prompt: "Please input your gender if you'd like to describe yourself.",
        name: 'Gender Text'
      },     
      {
        type: 'text',
        prompt: 'Please input your age in the text box below',
        name: 'Age',
        placeholder: 'digit only (e.g. 42)',
        input_type: 'number',
        required: true,
        required_error: "Please answer the question.",
        required_question_label: "*"
      },
      {
        type: 'multi-choice',
        prompt: "Are you color blind?", 
        name: 'Color blind', 
        options: ['Yes','No',"I don't know"], 
        required: true,
        required_error: "Please answer the question.",
        required_question_label: "*"
      }, 
      {
        type: 'multi-choice',
        prompt: "Which of the following describes your highest level of education?", 
        name: 'Education level', 
        options: ['High school graduate','Some college, no degree','Associates degree',"Bachelor's degree", 'Graduate degree (Masters, Doctorate, etc.)'], 
        required: true
      }],
      [
      {
        type: 'text',
        prompt: 'If applicable, could you tell us about your degree program?',
        name: 'program',
        placeholder: 'e.g. college major',
        required: false
      },
      {
        type: 'multi-choice',
        prompt: "How often do you come across animated charts when reading/watching TV/online?", 
        name: 'see animated chart', 
        options: ['Always','Very often','Sometimes','Rarely','Never'], 
        required: true,
        required_error: "Please answer the question.",
        required_question_label: "*"
      }, 
      {
        type: 'multi-choice',
        prompt: "Do you have any experience designing animated charts?", 
        name: 'design animated chart', 
        options: ['Yes','No'], 
        required: true,
        required_error: "Please answer the question.",
        required_question_label: "*"
      }, 
      {
        type: 'text',
        prompt: "Please briefly describe a time you design animated charts (If you answer 'Yes' in the previous question).", 
        name: 'design experience', 
        textbox_columns: 60,
        textbox_rows: 5,
        required: false
      }, 
]
      ]
};
  
timeline.push(demoQ);


function startExperiment(){
jsPsych.run(timeline);}