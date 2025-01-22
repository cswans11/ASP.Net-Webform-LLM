<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ChatLLM.aspx.cs" Inherits="LLMWebApp.ChatLLM" %>

<!DOCTYPE html>
<html>
<head>
    <title>Chat LLM</title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <h1>Chat with LLM</h1>
            <asp:Label ID="lblPrompt" runat="server" Text="Enter your question:"></asp:Label><br />
            <asp:TextBox ID="txtPrompt" runat="server" Width="400px"></asp:TextBox><br /><br />
            <asp:Button ID="btnSubmit" runat="server" Text="Generate Response" OnClick="btnSubmit_Click" />
            <br /><br />
            <asp:Label ID="lblResponse" runat="server" Text=""></asp:Label>
        </div>
    </form>
</body>
</html>