from Aoipy import Aoicogs
command = Aoicogs().Cogs
command(
    Name="Test",
    Code="$sendMessage[$currentChannelID[];This works]",
    Cog_Group="Testing"
)
