using System;
using System.IO;
using System.Net;
using System.Text;
using Newtonsoft.Json.Linq;
using System.Net.Sockets;
using System.Text;

namespace LLMWebApp
{
    public partial class ChatLLM : System.Web.UI.Page
    {
        protected void btnSubmit_Click(object sender, EventArgs e)
        {
            string prompt = txtPrompt.Text;
            string response = GetResponse(prompt);

            lblResponse.Text = $"Response: {response}";
        }

        public string GetResponse(string question)
        {
            using (var client = new TcpClient("127.0.0.1", 65432))
            using (var stream = client.GetStream())
            {
                byte[] data = Encoding.UTF8.GetBytes(question);
                stream.Write(data, 0, data.Length);

                byte[] buffer = new byte[1024];
                int bytesRead = stream.Read(buffer, 0, buffer.Length);
                return Encoding.UTF8.GetString(buffer, 0, bytesRead);
            }
        }
    }
}

