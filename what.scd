s.boot;



(
SynthDef.new(\chordTest, {
	arg amp=1.0;
	var sig1, sig2, sig3;
	sig1 = SinOsc.ar(440, mul: amp);
	sig2 = SinOsc.ar(523.25, mul: amp);
	sig3 = SinOsc.ar(659.23, mul: amp);
	Out.ar(0, sig1);
	Out.ar(0, sig2);
	Out.ar(0, sig3);
}).add;
)

x = Synth.new(\chordTest);

x.free;

(
w = Window.new("gui", Rect.new(750,50,500,200));
w.front;
w.alwaysOnTop_(True);

~slider = Slider.new(w.view, Rect.new(20,130,150,20)).action_({
	arg obj;
	var cf;
	cf = obj.value.postln;
	x.set(\amp, cf);
});
)

w.close;