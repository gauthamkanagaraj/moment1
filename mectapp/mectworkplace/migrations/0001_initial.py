# Generated by Django 3.1.1 on 2020-10-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bio',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('mobile', models.CharField(max_length=11, unique=True)),
                ('acctype', models.IntegerField(max_length=1)),
                ('designation', models.IntegerField(max_length=45)),
                ('profilepic', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('commentdata', models.CharField(max_length=45, null=True)),
                ('commenttime', models.CharField(max_length=35, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='darkmode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('dark', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='followers_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('groupid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='followers_people',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_to_follow', models.IntegerField()),
                ('id_follow', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('groupid', models.AutoField(primary_key=True, serialize=False)),
                ('adminid', models.IntegerField()),
                ('groupname', models.CharField(max_length=45, unique=True)),
                ('groupdp', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='joinrequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personid', models.IntegerField()),
                ('groupd', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('liketime', models.CharField(max_length=35, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='logout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('lflag', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='notificationcount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('nocount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ntime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('ptime', models.CharField(max_length=50)),
                ('etime', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('postid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField(null=True)),
                ('groupid', models.IntegerField()),
                ('postdata', models.CharField(max_length=500, null=True)),
                ('imgdata', models.CharField(max_length=100, null=True)),
                ('posttime', models.CharField(max_length=35, null=True)),
                ('likecount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='privatepost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('postid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='privatereply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idfrom', models.IntegerField()),
                ('idto', models.IntegerField()),
                ('replydata', models.CharField(max_length=200)),
                ('replytime', models.CharField(max_length=35, null=True)),
                ('postid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='userid',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddIndex(
            model_name='privatereply',
            index=models.Index(fields=['idfrom'], name='fk_privatereply_id1_idx'),
        ),
        migrations.AddIndex(
            model_name='privatereply',
            index=models.Index(fields=['idto'], name='fk_privatereply_id2_idx'),
        ),
        migrations.AddIndex(
            model_name='posts',
            index=models.Index(fields=['groupid'], name='fk_posts_groups1_idx'),
        ),
        migrations.AddIndex(
            model_name='posts',
            index=models.Index(fields=['userid'], name='fk_posts_id1_idx'),
        ),
        migrations.AddIndex(
            model_name='like',
            index=models.Index(fields=['postid'], name='fk_like_posts1_idx'),
        ),
        migrations.AddIndex(
            model_name='like',
            index=models.Index(fields=['userid'], name='fk_like_id1_idx'),
        ),
        migrations.AddIndex(
            model_name='joinrequest',
            index=models.Index(fields=['personid'], name='fk_joinrequest_id1_idx'),
        ),
        migrations.AddIndex(
            model_name='joinrequest',
            index=models.Index(fields=['groupd'], name='fk_joinrequest_groups1_idx'),
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['adminid'], name='fk_groups_id1_idx'),
        ),
        migrations.AddIndex(
            model_name='followers_people',
            index=models.Index(fields=['id_to_follow'], name='fk_followers_people_id1_idx'),
        ),
        migrations.AddIndex(
            model_name='followers_people',
            index=models.Index(fields=['id_follow'], name='fk_followers_people_id2_idx'),
        ),
        migrations.AddIndex(
            model_name='followers_group',
            index=models.Index(fields=['groupid'], name='fk_followers_group_groups1_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['postid'], name='fk_comment_posts1_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['userid'], name='fk_comment_id1_id'),
        ),
        migrations.AddIndex(
            model_name='bio',
            index=models.Index(fields=['userid'], name='fk_bio_id1_idx'),
        ),
    ]
