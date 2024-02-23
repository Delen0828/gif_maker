var jsPsych = initJsPsych();
var timeline = [];
const TRIALNUM=10

var chartReadIntro = {
  type: jsPsychHtmlKeyboardResponse,
  stimulus: 'You will now see 4 questions that each asks you to read a chart and answer a question related to the given chart.'
}
timeline.push(chartReadIntro)

var chartRead1 = {
  type: jsPsychImageButtonResponse,
  stimulus: './image/2.png',
  choices: ['60-70km', '30-40km', '20-30km', '50-60km'],
  //TODO: do we shuffle this?
  prompt: "What distance have customers traveled in the taxi the most?"
}
timeline.push(chartRead1)

var chartRead2 = {
  type: jsPsychImageButtonResponse,
  stimulus: './image/3.png',
  choices: ['Beijing','Shanghai','London','Seoul'],
  //TODO: do we shuffle this?
  prompt: "Which city’s metro system has the largest number of stations?"
}
timeline.push(chartRead2)

var chartRead3 = {
  type: jsPsychImageButtonResponse,
  stimulus: './image/4.png',
  choices: ['$50.54','$47.02','$42.34','43.48'],
  //TODO: do we shuffle this?
  prompt: "What was the price of a barrel of oil in February 2020?"
}
timeline.push(chartRead3)

var chartRead4 = {
  type: jsPsychImageButtonResponse,
  stimulus: 'image/1.png',
  choices: ['$0.71','$0.90','$0.80','$0.63'],
  //TODO: do we shuffle this?
  prompt: "What was the average price of a pound of coffee in October 2019?"
}
timeline.push(chartRead4)

//TODO: we are not goiong to do takeaway (written feedback) right?

var instructIntro = {
  type: jsPsychHtmlKeyboardResponse,
  stimulus: 'Next, we will look at two concepts that data analysts care a lot about when reading visualizations: mean and variance.'
}
timeline.push(instructIntro)

var meanDef = {
  type: jsPsychImageKeyboardResponse,
  stimulus_height: 525,
	stimulus_width: 809,
  stimulus: 'image/mean_sample.png',
  choices: "NO_KEYS",
  prompt: "<p>You see two sets of lines in the following visualizations, red and black. </p> <p>The <b>mean</b> value of the solid <b style='color:red'>red</b> line in this chart is measured by its overall position on the chart, as indicated by the red dashed line, which is approximately 4. The mean value of the solid <b>black</b> line is indicated by the black dashed line, which is approximately -4. </p> <p>With the vertical y-axis ranging from -20 to +20, we see that the higher the overall position of the line, the higher mean value it has.</p>",
  trial_duration: 5000  
};
timeline.push(meanDef)

var meanDefQ = {
  type: jsPsychImageButtonResponse,
  stimulus: 'image/mean_sample.png',
  stimulus_height: 525,
	stimulus_width: 809,
  choices: ['Black','Red','I have no idea'],
  //TODO: do we shuffle this?
  prompt: "Which line has the highest average?"
};
timeline.push(meanDefQ);

var varDef = {
  type: jsPsychImageKeyboardResponse,
  stimulus_height: 525,
	stimulus_width: 809,
  stimulus: 'image/mean_sample.png',
  choices: "NO_KEYS",
  prompt: "<p><b>Variance</b> is a measure of <b>how far</b> and <b>how frequently</b> the data is spread out from the mean. The farther and more frequently the data moves away from the mean, the higher the variance. </p> <p> In the chart below, the red area highlights the amount the red line spreads out from the mean. The gray area highlights the amount the black line spreads out from the mean. </p> <p> Approximately, the larger the area highlighted, the higher the variance.</p>",
  trial_duration: 5000  
};
timeline.push(varDef)

var varDefQ = {
  type: jsPsychImageButtonResponse,
  stimulus: 'image/variance_sample.png',
  stimulus_height: 525,
	stimulus_width: 809,
  choices: ['Black','Red','I have no idea'],
  //TODO: do we shuffle this?
  prompt: "Which line has the highest variance?"
};
timeline.push(varDefQ);


for (var rp=0;rp<TRIALNUM;rp++){
var pickID=jsPsych.randomization.randomInt(0,filelist.length)
var gif_name=filelist[pickID]
var gifShow = {
	stimulus_height: 480,
	stimulus_width: 640,
    type: jsPsychImageKeyboardResponse,
    stimulus: '../testgif/'+gif_name,
    choices: "NO_KEYS",
    prompt: "<p>Study this vis for 5 seconds.</p>",
	  render_on_canvas:false,
    trial_duration: 8000
	// stimulus_duration:4500
};
timeline.push(gifShow);

///---Option---///
const regex = /_([^_]+)\_[0-9].gif/;
const match = regex.exec(gif_name)[1];
// console.log(match)
var line_num=match.length
var Option = [];
for (var i=0;i<line_num;i++){
	var color=''
	switch(match[i]){
		case 'g' : color='Green'; break;
		case 'b' : color='Blue'; break;
		case 'y' : color='Yellow'; break;
		case 'p' : color='Purple'; break;
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
        "Which line has highest average?",
      options: Option,
      randomize_question_order: true,
      required: true,
    },
  ],
};
timeline.push(avgCheck);

Option = jsPsych.randomization.shuffle(Option);
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
timeline.push(varCheck);

}


jsPsych.run(timeline);