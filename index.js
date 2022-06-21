// Require the necessary default, discordJS and mongo classes
const fs = require('fs');
const { Client, Collection, Intents, MessageEmbed } = require('discord.js');
const { token, OpenAIKey } = require('./config.json');

//A couple fun things
const { AnnieRohnan, Marv, Jeremy, Geralt} = require('./strings.js');
const { Carrie, Tom } = require('./additionalStrings.js');

//OpenAI Setup
const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
	apiKey: OpenAIKey,
  });
  const openai = new OpenAIApi(configuration);
  var response = null;

// Create a new client instance
const client = new Client({
	intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES]
});

// Create commands list
client.commands = new Collection();
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
	const command = require(`./commands/${file}`);
	// Set a new item in the Collection
	// With the key as the command name and the value as the exported module
	client.commands.set(command.data.name, command);
}

// When the client is ready, run this code (only once)
client.once('ready', () => {
	console.log('Ready!');
});

// Run all slash commands here
client.on('interactionCreate', async interaction => {
	console.log("here");
	if (!interaction.isCommand()) return;

	const command = client.commands.get(interaction.commandName);

	if (!command) return;

	try {
		await command.execute(interaction);
	} catch (error) {
		console.error(error);
		await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
	}
});

//Check for new pings here
client.on("messageCreate", (message) => {
    if (message.author.bot) return false;
	
    if (message.content.includes("@here") || message.content.includes("@everyone") || message.type == "REPLY") return false;

    if (message.mentions.has(client.user.id)) {
		var response = "";
		if (message.content.substring(22, 27) == "reply") {
			response = "Me:" + message.content.substring(27) + "\n You:";
		} else if (message.content.substring(22, 36) == "Annie V Rohnan") {
			response = AnnieRohnan + message.content.substring(36);
		} else if (message.content.substring(22, 26) == "Marv") {
			response = Marv + message.content.substring(26) + "Marv:";
		} else if (message.content.substring(22, 28) == "Jeremy") {
			response = Jeremy + message.content.substring(28) + "Jeremy:";
		} else if (message.content.substring(22, 28) == "Geralt") {
			response = Geralt + message.content.substring(28) + "Geralt:";
		} else if (message.content.substring(22, 28) == "Carrie") {
			response = Carrie + message.content.substring(28) + "Carrie:";
		} else if (message.content.substring(22, 25) == "Tom") {
			response = Tom + message.content.substring(25) + "Tom:";
		} else {
			response = message.content.substring(22);
		}
		;(async () => {
			response = await openai.createCompletion({
			model: "text-davinci-002",
			prompt: response,
			temperature: 0.7,
			max_tokens: 512,
			top_p: 1,
			best_of: 1,
			frequency_penalty: 2,
			presence_penalty: 2,
			});
			//print the response text
			for(i of response.data.choices) {
				message.reply(i.text.substring(Math.max(i.length, 2000)))
			}
		})();
    }
});

// Login to Discord with your client's token
client.login(token);