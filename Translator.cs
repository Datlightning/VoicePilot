using DotnetGeminiSDK.Client.Interfaces;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.IO;
namespace translate
{
    public class Translator
    {
        private readonly GeminiClient _geminiClient;
        private readonly string _textInput;

        public Translator()
        {
            _textInput = File.ReadAllText(@"./input.txt");
            _geminiClient = new GeminiClient(new GoogleGeminiConfig
            {
                ApiKey = "AIzaSyB8a9s_JExxWHwvk1v1w2--tkmyvLHT2Z4"
            });
        }

        public async Task<string> Translate()
        {
            return await _geminiClient.TextPrompt(_textInput);
            
        }
    }
}