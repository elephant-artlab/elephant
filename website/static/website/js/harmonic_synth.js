$(document).ready(function() {

	var context = new webkitAudioContext();
	var oscillator_1, oscillator_2, oscillator_3, oscillator_4, oscillator_5;
	var gain_1, gain_2, gain_3, gain_4, gain_5;
	var playing;

	function startOsc(){

		playing = true;

		oscillator_1 = context.createOscillator();
		oscillator_2 = context.createOscillator();
		oscillator_3 = context.createOscillator();
		oscillator_4 = context.createOscillator();
		oscillator_5 = context.createOscillator();
		oscillator_1.type = 0;
		oscillator_2.type = 0;
		oscillator_3.type = 0;
		oscillator_4.type = 0;
		oscillator_5.type = 0;
		oscillator_1.frequency.value = document.querySelector('#frequency').value;
		oscillator_2.frequency.value = document.querySelector('#frequency').value * 2;
		oscillator_3.frequency.value = document.querySelector('#frequency').value * 3;
		oscillator_4.frequency.value = document.querySelector('#frequency').value * 4;
		oscillator_5.frequency.value = document.querySelector('#frequency').value * 5;
		gain_1 = context.createGainNode();
		gain_2 = context.createGainNode();
		gain_3 = context.createGainNode();
		gain_4 = context.createGainNode();
		gain_5 = context.createGainNode();
		gain_1.gain.value = document.querySelector('#volume-control-1').value;
		gain_2.gain.value = document.querySelector('#volume-control-2').value;
		gain_3.gain.value = document.querySelector('#volume-control-3').value;
		gain_4.gain.value = document.querySelector('#volume-control-4').value;
		gain_5.gain.value = document.querySelector('#volume-control-5').value;
		oscillator_1.connect(gain_1);
		oscillator_2.connect(gain_2);
		oscillator_3.connect(gain_3);
		oscillator_4.connect(gain_4);
		oscillator_5.connect(gain_5);
		gain_1.connect(context.destination);
		gain_2.connect(context.destination);
		gain_3.connect(context.destination);
		gain_4.connect(context.destination);
		gain_5.connect(context.destination);
		oscillator_1.noteOn(0);
		oscillator_2.noteOn(0);
		oscillator_3.noteOn(0);
		oscillator_4.noteOn(0);
		oscillator_5.noteOn(0);

	};

	function off() {

		playing = false;
		oscillator_1.noteOff(0);
		oscillator_2.noteOff(0);
		oscillator_3.noteOff(0);
		oscillator_4.noteOff(0);
		oscillator_5.noteOff(0);
		oscillator_1.disconnect();
		oscillator_2.disconnect();
		oscillator_3.disconnect();
		oscillator_4.disconnect();
		oscillator_5.disconnect();

	};

	$('#play-audio').click(function(){
		if (!playing){
			startOsc();
		}
	});

	$('#stop-audio').click(function(){
		off();
	});

	function controlVolume1(vol) {
		document.querySelector('#volume-1').value = vol;
		gain_1.gain.value = vol;
	}
	function controlVolume2(vol) {
		document.querySelector('#volume-2').value = vol;
		gain_2.gain.value = vol;
	}
	function controlVolume3(vol) {
		document.querySelector('#volume-3').value = vol;
		gain_3.gain.value = vol;
	}
	function controlVolume4(vol) {
		document.querySelector('#volume-4').value = vol;
		gain_4.gain.value = vol;
	}
	function controlVolume5(vol) {
		document.querySelector('#volume-5').value = vol;
		gain_5.gain.value = vol;
	}

	function controlFrequency(freq) {
		document.querySelector('#frequency').value = freq;
		oscillator_1.frequency.value = freq;
		oscillator_2.frequency.value = freq * 2;
		oscillator_3.frequency.value = freq * 3;
		oscillator_4.frequency.value = freq * 4;
		oscillator_5.frequency.value = freq * 5;
	}

});