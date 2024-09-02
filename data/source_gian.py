# coding: utf-8
df = pd.read_pickle('./genome.pkl')
t6novo = df[df.c100i100.isin(df[df.t6ss==True].c100i100)].t6ss
t6novo = t6novo.astype(bool)
df['is_fragment'] = False
df2 = df.neighbors(t6novo, after=5, before=5, min_block_distance=2)
