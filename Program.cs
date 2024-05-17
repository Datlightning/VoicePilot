using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.CognitiveServices.Speech;
using Microsoft.CognitiveServices.Speech.Audio;
using translate; 


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
	
	
	
	async static Task<string> translate(string input) {
		var tran = new translator(); 
		return translator.translate(input); 
		
	}

    async static Task Main(string[] args)
    {
        var speechConfig = SpeechConfig.FromSubscription("6addf40afc5c4398bb0da7c9b3ab7d25", "eastus");
        string result = await translate(await FromMic(speechConfig));
		Console.WriteLine(result); 
    }
}