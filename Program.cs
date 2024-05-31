using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.CognitiveServices.Speech;
using Microsoft.CognitiveServices.Speech.Audio;

using System.Diagnostics;
using System.Reflection;


class Program 
{
	
    async static Task<string> FromMic(SpeechConfig speechConfig)
    {
        using var audioConfig = AudioConfig.FromDefaultMicrophoneInput();
        using var speechRecognizer = new SpeechRecognizer(speechConfig, audioConfig);

        Console.WriteLine("Speak into your microphone.");
        var result = await speechRecognizer.RecognizeOnceAsync();
        return result.Text;
    }
	
    // from the voicepilot team, we would like to thank THERON WANG for finally contributing to his NJTSA PROJECT
    // we took this code from your hackMCST submission, so thank you so much. We love you THERON WANG!
    async static Task<string> translate(string input)
    {
        var processInfo = new ProcessStartInfo("python3")
        {
            ArgumentList = { "../../../translator.py", input},
            WorkingDirectory = Path.Join(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location)),
            RedirectStandardOutput = true
        };

        var process = Process.Start(processInfo);
        process!.BeginOutputReadLine();

        string output = "";

        process.OutputDataReceived += (object sender, DataReceivedEventArgs e) =>
        {
            output += e.Data;
        };

        await process.WaitForExitAsync();

        return output;
    }

    async static Task<string> getSpeech() {
        var speechConfig = SpeechConfig.FromSubscription("6addf40afc5c4398bb0da7c9b3ab7d25", "eastus");
        string result = await translate(await FromMic(speechConfig));
        return(result);
    }

    async static Task test() {

        // general things, dont delete this part of the test function.
        //this is useful for repetitive testing rather than having ruthvik scream COMMAND OPEN NOTEPAD iykyk
        Console.WriteLine("VOICE PILOT TEST FUNCTION");
        var testTranslate = "open notepad write hello world open chrome go to youtube move the mouse to the right three inches";

        // FROM HERE ON: TEST FUNCTION WRITE AWAY






    }

    async static Task main() {
        // THIS IS THE APPLICATION MAIN FUNCTION
        Console.WriteLine("This is the main function");
    }

    async static Task Main(string[] args)
    {
        test();
    }
}
