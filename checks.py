from main import *
def address_extraction_ip(old_mat):
    mat = [address for address in old_mat if "10" in address[1] or "192.168" in address[1]]
    return mat



def sensitive_format(old_mat):
    mat = [address for address in old_mat if address[3] == "22" or address[3] == "23" or address[3] == "3389"]
    return mat


def filter_by_size(old_mat):
    mat = [address for address in old_mat if address[-1] >= "5000"]
    return mat
# print(filter_by_size(sensitive_format(address_extraction_ip(list_fields(PATH_LOG)))))


def traffic_labeling(old_mat):
    mat = [(address ,"LARGE") if address[-1] >= "5000" else (address, "NORMAL") for address in old_mat]
    return mat
print(traffic_labeling(sensitive_format(address_extraction_ip(list_fields(PATH_LOG)))))