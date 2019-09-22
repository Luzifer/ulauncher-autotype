from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

import subprocess


class AutoType(Extension):

    def __init__(self):
        super(AutoType, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, AutoTypeExecute())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        items.append(ExtensionResultItem(icon='images/icon.svg',
                                         name='Auto-Type text...',
                                         description='Send text to foremost window using xdotool',
                                         on_enter=ExtensionCustomAction({
                                             "query": event.get_argument(),
                                         }, keep_app_open=False)))

        return RenderResultListAction(items)


class AutoTypeExecute(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()
        subprocess.check_call(['xdotool', 'type', data['query']])


if __name__ == '__main__':
    AutoType().run()
