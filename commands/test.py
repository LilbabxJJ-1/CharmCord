from Aoipy import cogs
command = cogs().Cogs
command(
    Name="Test",
    Code="$sendMessage[$currentChannelID[];This works]",
    Cog_Group="Testing"
)

command(
    Name="Test2",
    Code='$sendMessage[$currentChannelID[]; This works again]',
    Cog_Group="Testing"
)