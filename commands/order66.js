const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('order66')
		.setDescription('Executes Order 66'),
	async execute(interaction) {
        
        interaction.guild.members.cache.forEach(member => {
            if (member.voice.channel) {
                member.voice.disconnect('Order 66');
            }
        })

        return interaction.reply('Order 66 has been executed');
	},
};