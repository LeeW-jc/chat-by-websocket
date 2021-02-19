from flask import session
from flask_socketio import emit, join_room, leave_room
from .define_socket import wjc_socketio

print('导入文件')


@wjc_socketio.on('connect', namespace='/chat')
def connect():
    print('连接成功')


@wjc_socketio.on('joined', namespace='/chat')
def joined(information):
    # 'joined'路由是传入一个room_name,给该websocket连接分配房间,返回一个'status'路由
    room_name = information.get('client_to_server')
    user_name = session.get('user_name')
    join_room(room_name)
    emit('status', {'server_to_client': user_name + ' enter the room'}, room=room_name)


@wjc_socketio.on('left', namespace='/chat')
def left(information):
    # 传入 room_name 输出 系统消息
    room_name = information.get('client_to_server')
    user_name = session.get('user_name')
    leave_room(room_name)
    emit('status', {'server_to_client': user_name + ' has left the room'}, room=room_name)


@wjc_socketio.on('text', namespace='/chat')
def text(information):
    # 传入 room_name, text 输出text，user_name
    room_name = information.get('client_to_server')
    text = information.get('text')
    user_name = session.get('user_name')
    emit('message', {
        'user_name': user_name,
        'text': text,
    }, room=room_name)


