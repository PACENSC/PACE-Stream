import config

def change_channel(channelNo):
    config.switcher.setProgramInputVideoSource(0, channelNo)

def transition(channelNo):
    config.switcher.setPreviewInputVideoSource(0, channelNo)
    config.switcher.setMacroAction(config.switcher.atem.macros.macro1, config.switcher.atem.macroActions.runMacro)

def setup_GrandBallroom_GameRoom():
    config.switcher.setProgramInputVideoSource(0, config.switcher.atem.videoSources.superSource)

    # Enable both boxes
    config.switcher.setSuperSourceBoxParametersEnabled(0, True)  # Box 1
    config.switcher.setSuperSourceBoxParametersEnabled(1, True)  # Box 2

    # Set sources
    config.switcher.setSuperSourceBoxParametersInputSource(0, config.switcher.atem.cameras.camera3)  # Top half
    config.switcher.setSuperSourceBoxParametersInputSource(1, config.switcher.atem.cameras.camera4)  # Bottom half

    print("Setting Supersource parameters")

    config.switcher.setSuperSourceBoxParametersPositionX(0, 0)
    config.switcher.setSuperSourceBoxParametersPositionY(0, 0.5)
    config.switcher.setSuperSourceBoxParametersPositionX(1, 0)
    config.switcher.setSuperSourceBoxParametersPositionY(1, -0.5)
    config.switcher.setSuperSourceBoxParametersSize(1, 0.5)
    config.switcher.setSuperSourceBoxParametersSize(1, 0.5)

    print("Done!")

if __name__ == "__main__":
    config.init()
    transition(3)
    #change_channel(2)
    config.stop()

    


