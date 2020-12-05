from marketorestpython.client import MarketoClient
import sys, csv, os, pandas

export_file = 'C:/Talend/JobFiles/Marketo/Export/ActivityLog/ActivityLog_AType_41_50/file_mkto_actlog_atype_41_50_live.csv'

# SPECIFY CLIENT CREDENTIALS
munchkin_id =""
client_id = ""
client_secret = ""

mc = MarketoClient(munchkin_id, client_id, client_secret)

if __name__ == "__main__":
    a=0
    for activities in mc.execute(method='get_lead_activities_yield', activityTypeIds=['104','106','108','110','111','112','113','114','115','145'],
                                 nextPageToken=None, sinceDatetime=sys.argv[1], untilDatetime=sys.argv[2], listId=76414):

        records1 = pandas.DataFrame(index=range(0, len(activities)),
                                    columns=['MarketoGUID', 'Lead ID', 'Activity Date', 'Activity Type ID',
                                             'Primary Attribute Value Id', 'Primary Attribute Value', 'Attributes'])

        for index, item in enumerate(activities):
            if int(item["marketoGUID"]) > int(sys.argv[3]):
                records1.set_value(index, 'MarketoGUID', item["marketoGUID"])
                records1.set_value(index, 'Lead ID', item["leadId"])
                if 'activityDate' in item:
                    records1.set_value(index, 'Activity Date', item["activityDate"])
                if 'activityTypeId' in item:
                    records1.set_value(index, 'Activity Type ID', item["activityTypeId"])
                if 'primaryAttributeValueId' in item:
                    records1.set_value(index, 'Primary Attribute Value Id', item["primaryAttributeValueId"])
                if 'primaryAttributeValue' in item:
                    records1.set_value(index, 'Primary Attribute Value', item["primaryAttributeValue"])
                if 'attributes' in item:
                    records1.set_value(index, 'Attributes', item["attributes"])

        a = a + len(activities)
        print(a)
        records1.to_csv(export_file, sep=',', header=True, encoding='utf-8-sig', index=False, mode='a')