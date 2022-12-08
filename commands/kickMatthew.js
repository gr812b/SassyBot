const { SlashCommandBuilder } = require('@discordjs/builders');

const mattthewID = '386590321477419034';

module.exports = {
	data: new SlashCommandBuilder()
		.setName('kickmatt')
		.setDescription('Kicks Matthew from the VC Channel'),
	async execute(interaction) {
        // Gets member even when offline
        interaction.guild.members.fetch(mattthewID).then((matt) => {

            if (!matt.voice.channel) {
                return interaction.reply('No Matthew to bully');
            }

            interaction.guild.members.fetch(interaction.user.id).then(member => {
                if (member.voice.channel) {
                    // User is in a voice channel
                    matt.voice.disconnect('Sounds like a personal problem');
                    return interaction.reply('Matthew has been kicked from the VC Channel');
                } else {
                    // User is not in a voice channel
                    return interaction.reply('You are not in a voice channel');
                }
            });

            matt.send('Matthew L L L L L L L - ur a strinky pooo scrinny boi, get out of my vc. Begone thot');
        });
        
	},
};