from openerp.osv import fields, osv
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)

AVAILABLE_STATES =[
  ('draft','New'),
  ('open','Open'),
  ('active','Active'),
  ('done','Close'),
  ('blacklist','Blacklist'),
  ('delete','Deleted'),                        
]

AVAILABLE_REPORT_TYPE =[
  ('01','Master Customer'),
  ('02','Master Tenant'),
  ('03','Detail Redemption Transaction'),
  ('04','Summary Best Shopper'),
  ('05','Summary Tenant Sales'),
  ('06','Detail Reward Transaction'),
  ('07','Summary Credit Card'), 
  ('08','Detail Listing Coupon'),                       
]

class rdm_report(osv.osv_memory):
    _name = "rdm.report"
    
    def generate_report(self, cr, uid, ids, context=None):
        rdm_config = self.pool.get('rdm.config').get_config(cr, uid, context)
        params = self.browse(cr, uid, ids, context=context)
        param = params[0]   
        if param.report_id == '01':
            _logger.info("Start Master Customer Report")
            reportUnit = '/rdm/rdm_master_customer'
            serverUrl = 'http://' + rdm_config.report_server + ':' + rdm_config.report_server_port + '/jasperserver'
            j_username = rdm_config.report_user
            j_password = rdm_config.report_password
            ParentFolderUri = '/rdm'
            #reportUnit = '/rdm/detail_transaction'
            url = serverUrl + '/flow.html?_flowId=viewReportFlow&standAlone=true&_flowId=viewReportFlow&ParentFolderUri=' + ParentFolderUri + '&reportUnit=' + reportUnit + '&decorate=no&j_username=' + j_username + '&j_password=' + j_password
            return {
                'type':'ir.actions.act_url',
                'url': url,
                'nodestroy': True,
                'target': 'new' 
            }
                      
            
        if param.report_id == '02':
            _logger.info("Start Master Tenant Report")
            reportUnit = '/rdm/rdm_master_tenant'
            serverUrl = 'http://' + rdm_config.report_server + ':' + rdm_config.report_server_port + '/jasperserver'
            j_username = rdm_config.report_user
            j_password = rdm_config.report_password
            ParentFolderUri = '/rdm'
            #reportUnit = '/rdm/detail_transaction'
            url = serverUrl + '/flow.html?_flowId=viewReportFlow&standAlone=true&_flowId=viewReportFlow&ParentFolderUri=' + ParentFolderUri + '&reportUnit=' + reportUnit + '&decorate=no&j_username=' + j_username + '&j_password=' + j_password
            return {
                'type':'ir.actions.act_url',
                'url': url,
                'nodestroy': True,
                'target': 'new' 
            }
            
            
        if param.report_id == '03':
            _logger.info("Start Detail Transaction Report")
            reportUnit = '/rdm/rdm_daily_transaction_report'
            serverUrl = 'http://' + rdm_config.report_server + ':' + rdm_config.report_server_port + '/jasperserver'
            j_username = rdm_config.report_user
            j_password = rdm_config.report_password
            ParentFolderUri = '/rdm'
            report_params= '&START_DATE=' + param.start_date + '&END_DATE=' + param.end_date + '&STATE=' + param.state
            #reportUnit = '/rdm/detail_transaction'
            url = serverUrl + '/flow.html?_flowId=viewReportFlow&standAlone=true&_flowId=viewReportFlow&ParentFolderUri=' + ParentFolderUri + '&reportUnit=' + reportUnit + report_params + '&decorate=no&j_username=' + j_username + '&j_password=' + j_password
            return {
                'type':'ir.actions.act_url',
                'url': url,
                'nodestroy': True,
                'target': 'new' 
            }
            
        
        if param.report_id == '04':
            _logger.info("Start Summary Best Shopper Report")
            reportUnit = '/rdm/rdm_sum_best_shopper_report'
            serverUrl = 'http://' + rdm_config.report_server + ':' + rdm_config.report_server_port + '/jasperserver'
            j_username = rdm_config.report_user
            j_password = rdm_config.report_password
            ParentFolderUri = '/rdm'
            report_params= '&START_DATE=' + param.start_date + '&END_DATE=' + param.end_date
            #reportUnit = '/rdm/detail_transaction'
            url = serverUrl + '/flow.html?_flowId=viewReportFlow&standAlone=true&_flowId=viewReportFlow&ParentFolderUri=' + ParentFolderUri + '&reportUnit=' + reportUnit + report_params + '&decorate=no&j_username=' + j_username + '&j_password=' + j_password
            return {
                'type':'ir.actions.act_url',
                'url': url,
                'nodestroy': True,
                'target': 'new' 
            }    
                     
        if param.report_id == '05':
            _logger.info("Start Summary Tenant Sales Report")
            reportUnit = '/rdm/rdm_sum_tenant_sales_report'
            serverUrl = 'http://' + rdm_config.report_server + ':' + rdm_config.report_server_port + '/jasperserver'
            j_username = rdm_config.report_user
            j_password = rdm_config.report_password
            ParentFolderUri = '/rdm'
            report_params= '&START_DATE=' + param.start_date + '&END_DATE=' + param.end_date
            #reportUnit = '/rdm/detail_transaction'
            url = serverUrl + '/flow.html?_flowId=viewReportFlow&standAlone=true&_flowId=viewReportFlow&ParentFolderUri=' + ParentFolderUri + '&reportUnit=' + reportUnit + report_params + '&decorate=no&j_username=' + j_username + '&j_password=' + j_password
            return {
                'type':'ir.actions.act_url',
                'url': url,
                'nodestroy': True,
                'target': 'new' 
            }    
            
        
        if param.report_id == '06':
            _logger.info("Start Detail Reward Transaction Report")
            reportUnit = '/rdm/rdm_detail_reward_trans_report'
            serverUrl = 'http://' + rdm_config.report_server + ':' + rdm_config.report_server_port + '/jasperserver'
            j_username = rdm_config.report_user
            j_password = rdm_config.report_password
            ParentFolderUri = '/rdm'
            report_params= '&START_DATE=' + param.start_date + '&END_DATE=' + param.end_date + '&STATE=' + param.state
            #reportUnit = '/rdm/detail_transaction'
            url = serverUrl + '/flow.html?_flowId=viewReportFlow&standAlone=true&_flowId=viewReportFlow&ParentFolderUri=' + ParentFolderUri + '&reportUnit=' + reportUnit + report_params + '&decorate=no&j_username=' + j_username + '&j_password=' + j_password
            return {
                'type':'ir.actions.act_url',
                'url': url,
                'nodestroy': True,
                'target': 'new' 
            }    
                   
        if param.report_id == '07':
            _logger.info("Start Summary Credit Card Report")
            reportUnit = '/rdm/rdm_sum_credit_card_report'
            serverUrl = 'http://' + rdm_config.report_server + ':' + rdm_config.report_server_port + '/jasperserver'
            j_username = rdm_config.report_user
            j_password = rdm_config.report_password
            ParentFolderUri = '/rdm'
            report_params= '&START_DATE=' + param.start_date + '&END_DATE=' + param.end_date
            #reportUnit = '/rdm/detail_transaction'
            url = serverUrl + '/flow.html?_flowId=viewReportFlow&standAlone=true&_flowId=viewReportFlow&ParentFolderUri=' + ParentFolderUri + '&reportUnit=' + reportUnit + report_params + '&decorate=no&j_username=' + j_username + '&j_password=' + j_password
            return {
                'type':'ir.actions.act_url',
                'url': url,
                'nodestroy': True,
                'target': 'new' 
            }
      
        if param.report_id == '08':
            _logger.info("Start Detail Listing Coupon Report")
            reportUnit = '/rdm/rdm_detail_listing_coupon_report'
            serverUrl = 'http://' + rdm_config.report_server + ':' + rdm_config.report_server_port + '/jasperserver'
            j_username = rdm_config.report_user
            j_password = rdm_config.report_password
            ParentFolderUri = '/rdm'
            report_params= '&START_DATE=' + param.start_date + '&END_DATE=' + param.end_date
            #reportUnit = '/rdm/detail_transaction'
            url = serverUrl + '/flow.html?_flowId=viewReportFlow&standAlone=true&_flowId=viewReportFlow&ParentFolderUri=' + ParentFolderUri + '&reportUnit=' + reportUnit + report_params + '&decorate=no&j_username=' + j_username + '&j_password=' + j_password
            return {
                'type':'ir.actions.act_url',
                'url': url,
                'nodestroy': True,
                'target': 'new' 
            }
        
    _columns = {
        'report_id' : fields.selection(AVAILABLE_REPORT_TYPE,'Report Name', size=16, required=True),        
        'start_date': fields.date('Start Date'),
        'end_date': fields.date('End Date'),
        'state': fields.selection(AVAILABLE_STATES,'Status', size=16),                        
    }
    
rdm_report()


    
    
    