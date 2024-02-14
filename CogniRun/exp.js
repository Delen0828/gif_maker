var jsPsych = initJsPsych();
var timeline = [];
const TRIALNUM=10


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
    trial_duration: 5000
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
		case 'r' : color='Red'; break;
		case 'y' : color='Yellow'; break;
		case 'b' : color='Blue'; break;
		case 'o' : color='Orange'; break;
		default: color='NOT_DEFINED'; break;
	}
	Option.push(color);
}

Option = jsPsych.randomization.shuffle(Option);
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

}


jsPsych.run(timeline);