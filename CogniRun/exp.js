var jsPsych = initJsPsych();

var timeline = [];
var gif_name = './trace_AVG[-5, 5]_VAR[3, 3]_SPIKE[0, 1]_rb.gif'
//TODO: This will be sampled from seq_notrace_his for 5/6
var gifShow = {
	stimulus_height: 480,
	stimulus_width: 640,
    type: jsPsychImageKeyboardResponse,
    stimulus: gif_name,
    choices: "NO_KEYS",
    prompt: "<p>Study this vis for 5 seconds.</p>",
	render_on_canvas:false,
    trial_duration: 4000
	// stimulus_duration:4500
};

timeline.push(gifShow);
const regex = /_([^_]+)\.gif/;

const match = regex.exec(gif_name)[1];
console.log(match)
var line_num=match.length
var Option = [
];
for (var i=0;i<line_num;i++){
	var color=''
	switch(match[i]){
		case 'r' : color='Red'; break;
		case 'y' : color='Yellow'; break;
		case 'b' : color='Blue'; break;
		case 'k' : color='Black'; break;
	}
	Option.push(color);
}

Option = jsPsych.randomization.shuffle(Option);
// create check
var attnCheck = {
  type: jsPsychSurveyMultiChoice,
  questions: [
    {
      prompt:
        "Which line has highest average?",
      name: "AttnChk",
      options: Option,
      randomize_question_order: true,
      required: true,
    },
  ],
};

timeline.push(attnCheck);



jsPsych.run(timeline);