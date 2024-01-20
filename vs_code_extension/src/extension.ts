import * as path from "path";
import * as vscode from "vscode";

async function launchChromeApp(context: vscode.ExtensionContext) {
  try {
    // Dynamic import using 'await'
    const chromeLauncher = await import("chrome-launcher");

    chromeLauncher.launch({
      chromeFlags: [
        `--app=file://${path
          .join(context.extensionPath, "camera", "camera.html")
          .replace("\\", "/")}`,
      ],
    });
  } catch (error) {
    console.error("Error launching Chrome:", error);
  }
}

export function activate(context: vscode.ExtensionContext) {
  // Register a command that shows VSCode camera feed in a Chrome window.
  context.subscriptions.push(
    vscode.commands.registerCommand("jutsuclip.start", async () => {
      // You can replace this with your custom 'bark' functionality
      // Call the common function for launching Chrome
      await launchChromeApp(context);
    })
  );

  context.subscriptions.push(
    vscode.commands.registerCommand("jutsuclip.meow", async () => {
      vscode.window.showInformationMessage("Meow!");
    })
  );

  const panel = vscode.window.createWebviewPanel(
    "cameraFeed",
    "Camera Feed",
    vscode.ViewColumn.One,
    {
      enableScripts: true,
      retainContextWhenHidden: true,
      localResourceRoots: [
        vscode.Uri.file(path.join(context.extensionPath, "camera")),
      ],
      // Add contentSecurityPolicy as needed
      // contentSecurityPolicy: {...},
    }
  );

  // Set basic HTML content with the local image
  const htmlContent = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Camera Feed</title>
    </head>
    <body>
      <h1>Welcome to the Camera Feed</h1>
      <p>This is some basic HTML content.</p>
      <button onclick="captureScreenshot()">Capture Screenshot</button>
    </body>
    <script>
      function captureScreenshot() {
        // Send a message to the extension to capture a screenshot
        vscode.postMessage({ command: "captureScreenshot" });
      }
    </script>
    </html>
  `;

  panel.webview.html = htmlContent;

  // Handle messages from the webview
  panel.webview.onDidReceiveMessage((message) => {
    // Show an information message with the received message
    vscode.window.showInformationMessage(
      `Received message: ${JSON.stringify(message)}`
    );

    // Check the command and perform corresponding actions
    if (message.command === "captureScreenshot") {
      // Show a message in VS Code indicating the captureScreenshot command is received
      vscode.window.showInformationMessage("Bark!");

      // Call the captureScreenshot function
      captureScreenshot();
    } else if (message.command === "customCommand") {
      // Handle the custom command with additional data
      handleCustomCommand(message.data);
    }
  });

  // Function to capture and save a screenshot
  function captureScreenshot() {
    // Logic for capturing and saving the screenshot
    vscode.window.showInformationMessage("Screenshot captured!");
  }

  // Function to handle a custom command with additional data
  function handleCustomCommand(data: string) {
    // Logic for handling the custom command with additional data
    vscode.window.showInformationMessage(
      `Custom command received. Additional data: ${data}`
    );
  }
}

export function deactivate() {}
