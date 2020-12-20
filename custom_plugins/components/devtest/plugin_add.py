# -*- coding:utf-8 -*-
# @author: sky
# @Time: 
# @Email: sky@canway.net

# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from pipeline.conf import settings
from pipeline.core.flow.activity import Service, StaticIntervalGenerator
from pipeline.component_framework.component import Component

__group_name__ = _(u"测试开发插件(CDP)")


class NodeAddService(Service):
    __need_schedule__ = False

    def execute(self, data, parent_data):
        try:
            add_arg1 = data.get_one_of_inputs('add_arg1')
            add_arg2 = data.get_one_of_inputs('add_arg2')
            summary = int(add_arg1) + int(add_arg2)
            data.set_outputs('sum', summary)
            data.set_outputs('message', 'compute success')
            return True
        except Exception as e:
            err_msg = e.message if e.message else str(e)
            data.set_outputs('sum', '')
            data.set_outputs('message', str(err_msg))
            return False

    def schedule(self, data, parent_data, callback_data=None):
        return True

    def outputs_format(self):
        return [
            self.OutputItem(name=_(u'结果'), key='result', type='str'),
            self.OutputItem(name=_(u'summary'), key='sum', type='str'),
            self.OutputItem(name=_(u'执行信息'), key='message', type='str')
        ]


class NodeAddComponent(Component):
    name = _(u'加法')
    code = 'cdp_node_add'
    bound_service = NodeAddService
    embedded_form = True
    form = """
(function(){
    $.atoms.cdp_node_add = [
        {
            tag_code: "add_arg1",
            type: "input",
            attrs: {
                name: gettext("plus1"),
                placeholder: gettext("请输入数字"),
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
        {
            tag_code: "add_arg2",
            type: "input",
            attrs: {
                name: gettext("plus2"),
                placeholder: gettext("请输入数字"),
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        }
    ]
})();
"""

