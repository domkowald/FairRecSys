# print the track/artist distributions for users and countries to txt files
# + print the track/artist - user matrix to scipy sparse matrix format
# this script needs the LFM-1b_users.txt and LFM-1b_LEs.txt in a 'data' folder

import pandas as pd
import scipy.sparse
import sys
type = 'artist'

# get user data
pd_users = pd.read_csv('data/LFM-1b_users.txt', sep='\t')
pd_users['user_id'] = pd_users['user_id'].astype(str)
pd_users = pd_users.set_index('user_id')
print('Total users: ' + str(len(pd_users)))
sys.stdout.flush()

# remove users without country information
pd_users = pd_users.dropna(subset=['country'])
print('Users with country information: ' + str(len(pd_users)))
sys.stdout.flush()

# how many distinct countries?
print('Distinct countries: ' + str(len(pd_users['country'].unique())))
sys.stdout.flush()

# test output
if '384' in pd_users.index:
    print('Country of user 384: ' + pd_users.loc['384']['country'])
    sys.stdout.flush()

# get distributions
l_count = 0
track_dist = dict() # track-distribution
user_dist = dict() # user-distribution
country_dist = dict() # country-distribution
user_dict = dict() # for each user -> track-distribution
country_dict = dict() # for each country -> track-distribution
country_user_dict = dict() # for each country -> user-distribution
with open('data/LFM-1b_LEs.txt', mode='r') as f:
    for l in f:
        vals = l.split('\t')
        user = vals[0]
        # use only events of users with country information
        if user in pd_users.index:
            l_count += 1
            country = pd_users.loc[user]['country']
            if type == 'track':
                track = vals[3]
            else:
                track = vals[1]
            
            if user in user_dict:
                u_dict = user_dict[user]
            else:
                u_dict = dict()
                user_dict[user] = u_dict
            if country in country_dict:
                c_dict = country_dict[country]
            else:
                c_dict = dict()
                country_dict[country] = c_dict
            if country in country_user_dict:
                cu_dict = country_user_dict[country]
            else:
                cu_dict = dict()
                country_user_dict[country] = cu_dict
                
            if track in track_dist:
                track_dist[track] += 1
            else:
                track_dist[track] = 1
            if user in user_dist:
                user_dist[user] += 1
            else:
                user_dist[user] = 1
            if country in country_dist:
                country_dist[country] += 1
            else:
                country_dist[country] = 1
                
            if track in u_dict:
                u_dict[track] += 1
            else:
                u_dict[track] = 1
            if track in c_dict:
                c_dict[track] += 1
            else:
                c_dict[track] = 1
            if user in cu_dict:
                cu_dict[user] += 1
            else:
                cu_dict[user] = 1
            if l_count % 1000000 == 0: # output after 1M lines
                print('Lines processed: ' + str(l_count))
                sys.stdout.flush()
print('Finished, processed lines: ' + str(l_count))
sys.stdout.flush()

# print sorted user distribution
sorted_users = sorted(user_dist.items(), key = lambda x:x[1], reverse = True)
with open('data/user_dist.txt', mode='w') as f:
    for u, count in sorted_users:
        f.write(u + '\t' + str(count) + '\n')

# print sorted track/artist distribution
sorted_tracks = sorted(track_dist.items(), key = lambda x:x[1], reverse = True)
with open('data/' + type + '_dist.txt', mode='w') as f:
    for t, count in sorted_tracks:
        f.write(t + '\t' + str(count) + '\n')

# print sorted country distribution
sorted_countries = sorted(country_dist.items(), key = lambda x:x[1], reverse = True)
with open('data/country_dist.txt', mode='w') as f:
    for c, count in sorted_countries:
        f.write(c + '\t' + str(count) + '\n')
        
# print sorted tracks/artists-per-user distribution
with open('data/user_' + type + '_dist.txt', mode='w') as f:
    for u, u_dict in user_dict.items():
        f.write(u + '\t')
        sorted_users = sorted(u_dict.items(), key = lambda x:x[1], reverse = True)
        for t, count in sorted_users:
            f.write(t + ' ' + str(count) + ';')
        f.write('\n')

# print sorted tracks/artists-per-country distribution
with open('data/country_' + type + '_dist.txt', mode='w') as f:
    for c, c_dict in country_dict.items():
        f.write(c + '\t')
        sorted_countries = sorted(c_dict.items(), key = lambda x:x[1], reverse = True)
        for t, count in sorted_countries:
            f.write(t + ' ' + str(count) + ';')
        f.write('\n')

# print sorted users-per-country distribution
with open('data/country_user_dist.txt', mode='w') as f:
    for c, cu_dict in country_user_dict.items():
        f.write(c + '\t')
        sorted_countries = sorted(cu_dict.items(), key = lambda x:x[1], reverse = True)
        for t, count in sorted_countries:
            f.write(t + ' ' + str(count) + ';')
        f.write('\n')
        
# print the sparse matrix
row = []
col = []
val = []

with open('data/user_' + type + '_dist.txt') as f:
    for line in f:
        user, tracks = line.split('\t', 1)
        for t_parts in tracks[:-2].split(';'):
            track, count = t_parts.split(' ', 1)
            row.append(int(user))
            col.append(int(track))
            val.append(int(count))

print(len(row))
print(len(col))
print(len(val))
sys.stdout.flush()

sparse_matrix = scipy.sparse.coo_matrix((val, (row, col)))
print(sparse_matrix.getnnz())
sys.stdout.flush()

scipy.sparse.save_npz('data/' + type + '_matrix.npz', sparse_matrix)
test_matrix = scipy.sparse.load_npz('data/' + type + '_matrix.npz')
print(test_matrix.getnnz())
sys.stdout.flush()
