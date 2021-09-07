from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response

from .models import User, Room
from .serializers import UserSerializer, UserListSerializer, RoomSerializer, RoomListSerializer


class UserListCreateAPIView(views.APIView):
    """ユーザモデルの取得(一覧)・登録APIクラス"""

    def get(self, request, *args, **kwargs):
        """ユーザモデルの取得(一覧)APIに対応するハンドラメソッド"""

        # モデルオブジェクトの一覧を取得
        user_list = User.objects.all()
        # シリアライザオブジェクトを作成
        serializer = UserSerializer(instance=user_list, many=True)
        # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        """ユーザモデルの登録APIに対応するハンドラメソッド"""

        # 子ラリアライザオブジェクトを作成
        serializer = UserSerializer(data=request.data)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを登録
        serializer.save()
        # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyAPIView(views.APIView):
    """ユーザモデルの取得(詳細)・更新・一部更新・削除APIクラス"""

    def get(self, request, pk, *args, **kwargs):
        """ユーザモデルの取得(詳細)APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        user = get_object_or_404(User, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = UserSerializer(instance=user)
        # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        """ユーザモデルの更新APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        user = get_object_or_404(User, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = UserSerializer(instance=user, data=request.data)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを更新
        serializer.save()
        # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        """ユーザモデルの一部更新APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        user = get_object_or_404(User, pk=pk)
        # モデルオブジェクトを作成
        serializer = UserSerializer(
            instance=user, data=request.data, partial=True)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを一部更新
        serializer.save()
        # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        """ユーザモデルの削除APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        user = get_object_or_404(User, pk=pk)
        # モデルオブジェクトを削除
        user.delete()
        # レスポンスオブジェクトを返す
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoomListCreateAPIView(views.APIView):
    """ルームモデルの取得(一覧)・登録APIクラス"""

    def get(self, request, *args, **kwargs):
        """ルームモデルの取得(一覧)APIに対応するハンドラメソッド"""

        # モデルオブジェクトの一覧を取得
        room_list = Room.objects.all()
        # シリアライザオブジェクトを作成
        serializer = RoomSerializer(instance=room_list, many=True)
        # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        """ルームモデルの登録APIに対応するハンドラメソッド"""

        # 子ラリアライザオブジェクトを作成
        serializer = RoomSerializer(data=request.data)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを登録
        serializer.save()
        # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_201_CREATED)


class RoomRetrieveUpdateDestroyAPIView(views.APIView):
    """ルームモデルの取得(詳細)・更新・一部更新・削除APIクラス"""

    def get(self, request, pk, *args, **kwargs):
        """ルームモデルの取得(詳細)APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        room = get_object_or_404(Room, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = RoomSerializer(instance=room)
        # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        """ルームモデルの更新APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        room = get_object_or_404(Room, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = RoomSerializer(instance=room, data=request.data)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを更新
        serializer.save()
        # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        """ルームモデルの一部更新APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        room = get_object_or_404(Room, pk=pk)
        # モデルオブジェクトを作成
        serializer = RoomSerializer(
            instance=room, data=request.data, partial=True)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを一部更新
        serializer.save()
        # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        """ロームモデルの削除APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        room = get_object_or_404(User, pk=pk)
        # モデルオブジェクトを削除
        room.delete()
        # レスポンスオブジェクトを返す
        return Response(status=status.HTTP_204_NO_CONTENT)
