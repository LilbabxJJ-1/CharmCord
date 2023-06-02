from Aoipy import Aoicogs
command = Aoicogs().Cogs
command(
    Name="Tests",
    Code="$sendMessage[$currentChannelID[];This works]",
    Cog_Group="Testing"
)
