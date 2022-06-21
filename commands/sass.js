const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('sass')
		.setDescription('Replies with Sass!'),
	async execute(interaction) {
		return interaction.reply('Fuck you');
	},
};